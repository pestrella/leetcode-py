def syntax_tree(s, multiply=[], add=[]):
    if len(s) > 0:
        c = s[0]
        if c == '+':
            add.append(multiply)
            multiply = []

        elif c == '*':
            pass

        else:
            multiply.append(ord(c) - 48)

        return syntax_tree(s[1:], multiply=multiply, add=add)
    else:
        if len(multiply) > 0:
            add.append(multiply)

        return add
