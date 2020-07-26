def braces_match(s):
    stack = []
    for c in s:
        if c in {'(', '{', '['}:
            stack.append(c)
        elif c in {')', '}', ']'}:
            last_brace = stack.pop()
            if not is_brace_pair(last_brace, c):
                return False

    return not stack


def is_brace_pair(a, b):
    if a == '(':
        return b == ')'
    if a == '{':
        return b == '}'
    if a == '[':
        return b == ']'

    return False
