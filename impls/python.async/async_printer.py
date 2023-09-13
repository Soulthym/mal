def pr_str(ast):
    if isinstance(ast, list):
        return f"({' '.join(map(pr_str, ast))})"
    return str(ast)
