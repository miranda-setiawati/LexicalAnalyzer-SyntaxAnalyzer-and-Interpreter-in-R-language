import sys
from syntax_analyzer import parse

# Environment to store variables
environment = {}

def evaluate(node):
    if isinstance(node, tuple):
        if node[0] == 'print':
            value = evaluate(node[1])
            print(value.strip('"'))  # Remove surrounding quotes
        elif node[0] == 'cat':
            args = [evaluate(arg) for arg in node[1]]
            print(''.join(str(arg).strip('"') for arg in args), end="")
        elif node[0] == 'assign':
            environment[node[1]] = evaluate(node[2])
        elif node[0] == 'binop':
            left = evaluate(node[2])
            right = evaluate(node[3])
            if node[1] == '+':
                return left + right
            elif node[1] == '/':
                return left / right
            elif node[1] == '%':
                return left % right
            elif node[1] == '>':
                return left > right
            elif node[1] == '<=':
                return left <= right
            elif node[1] == '!=':
                return left != right
        elif node[0] == 'number':
            return node[1]
        elif node[0] == 'string':
            return node[1]
        elif node[0] == 'id':
            return environment.get(node[1], 0)  # Default value is 0
        elif node[0] == 'while':
            condition = node[1]
            body = node[2]
            while evaluate(condition):
                for stmt in body:
                    evaluate(stmt)
        elif node[0] == 'if':
            condition = node[1]
            if_block = node[2]
            else_block = node[3]  # Blok else

            if evaluate(condition):
                for stmt in if_block:
                    evaluate(stmt)
            elif else_block:  # Evaluasi blok else jika tersedia
                for stmt in else_block:
                    evaluate(stmt)

    return node

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        code = f.read()

    try:
        ast = parse(code)
        if ast:
            for stmt in ast:
                evaluate(stmt)
    except Exception as e:
        print(f"Error: {e}")
