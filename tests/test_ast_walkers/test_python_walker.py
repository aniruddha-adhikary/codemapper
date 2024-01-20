import ast
from codemapper.ast_walkers.python_walker import augment_summary


def test_augment_summary_for_docstring_and_pass():
    input_code = """
def test_function(x, y):
    result = x + y
    return result
"""
    output = augment_summary(input_code)
    output_tree = ast.parse(output)

    # Check if each function has exactly a docstring and a pass statement
    for node in ast.walk(output_tree):
        if isinstance(node, ast.FunctionDef):
            assert len(node.body) == 2, "Function body does not contain exactly two nodes."
            assert isinstance(node.body[0], ast.Expr), "First node in function body is not a docstring."
            assert isinstance(node.body[1], ast.Pass), "Second node in function body is not a pass statement."
