def calc(s):
    out = []
    operators = []

    for c in s:
        if is_num(c):
            out.append(ord(c) - 48)
        elif c in {'+', '-', '*', '/'}:
            while operators and has_precedence(operators[-1], c):
                out.append(operators.pop())

            operators.append(c)

    while operators:
        out.append(operators.pop())

    print(f"rpn: {out}")
    return reduce_rpn(out)


def reduce_rpn(arr):
    if len(arr) == 1:
        return arr[0]

    out = []
    for i in arr:
        if isinstance(i, int):
            out.append(i)
        else:
            right = out.pop()
            left = out.pop()
            out.append(do_math(i, left, right))

    return reduce_rpn(out)


def do_math(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2


def is_num(c):
    return ord(c) > 47 and ord(c) < 58


def has_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence[op1] >= precedence[op2]
