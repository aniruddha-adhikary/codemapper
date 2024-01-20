import ast

import astor
import requests

from codemapper.augmentation import summarise_code, summarise_class, summarise_file


class FuncSummariser(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        summary = summarise_code(astor.to_source(node))

        docstring_node = ast.Expr(value=ast.Constant(value=summary))

        node.body = [docstring_node, ast.Pass()]
        return node


class ClassSummariser(ast.NodeTransformer):
    def visit_ClassDef(self, node):
        summary = summarise_class(astor.to_source(node))

        docstring_node = ast.Expr(value=ast.Constant(value=summary))

        node.body.insert(0, docstring_node)
        return node


def summarize_module(tree):
    summary = summarise_file(astor.to_source(tree))

    # Create a docstring node
    docstring_node = ast.Expr(value=ast.Constant(value=summary))

    # Insert the docstring at the beginning of the module
    tree.body.insert(0, docstring_node)

    return tree


def augment_summary(code):
    tree = ast.parse(code)

    FuncSummariser().visit(tree)
    ClassSummariser().visit(tree)
    summarize_module(tree)

    code = astor.to_source(tree)
    return code


if __name__ == "__main__":
    print(augment_summary(requests.get('https://raw.githubusercontent.com/impira/docquery/main/src/docquery/ocr_reader.py').text))
