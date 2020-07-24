from functools import reduce

def syntax_tree(s):
    """Can parse simple syntax like `4+2*3`"""

    additions = []
    multiplications = []

    for c in s:
        if c == '+':
            additions.append(multiplications)
            multiplications = []

        elif c == '*':
            pass

        else:
            multiplications.append(ord(c) - 48)

    if len(multiplications) > 0:
        additions.append(multiplications)

    return sum(list(map(multiply, additions)))

def multiply(nums):
    return reduce(lambda n, m: n * m, nums)

def sum(nums):
    return reduce(lambda n, m: n + m, nums)
