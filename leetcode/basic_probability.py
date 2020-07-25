from leetcode.basic_math import gcd

def two_dice(n):
    """
    Given 2 dice, return the probability that the thrown sum is
    at most n.
    """

    sums = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j <= n:
                sums.append((i, j))

    numerator = len(sums)
    denominator = 36

    greatest_common_divisor = gcd(numerator, denominator)
    return "%d/%d" % (numerator / greatest_common_divisor,
                      denominator / greatest_common_divisor)
