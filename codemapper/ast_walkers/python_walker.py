import ast

import astor

from codemapper.augmentation import summarise_code


class FuncSummariser(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        summary = summarise_code(astor.to_source(node))

        docstring_node = ast.Expr(value=ast.Constant(value=f"{summary}"))

        node.body = [docstring_node, ast.Pass()]
        return node


def augment_summary(code):
    tree = ast.parse(code)
    FuncSummariser().visit(tree)

    return astor.to_source(tree)
