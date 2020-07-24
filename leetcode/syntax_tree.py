from functools import reduce

def syntax_tree(s):
    """Can parse simple syntax like `4+2*3`g"""

    add = []
    multiply = []
    for c in s:
        if c == '+':
            add.append(multiply)
            multiply = []

        elif c == '*':
            pass

        else:
            multiply.append(ord(c) - 48)

    if len(multiply) > 0:
        add.append(multiply)

    return reduce(lambda n, m: n + m
                  , list(map(lambda nums: reduce(lambda n, m: n * m, nums)
                             , add)))
