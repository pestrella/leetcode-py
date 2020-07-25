from functools import reduce


def get_averages(node):
    """
    Given a binary tree, compute the average number at each depth
    e.g.--
    Input:
         8
        / \
       /   \
      4    15
     / \   / \
    2   6 9  22
       /    /
      5    17

    Output: [8, 9.5, 9.75, 11]
    """
    depths = get_depths(node)
    return [average(values) for depth, values in depths.items()]


def get_depths(node, data=None, depth=0):
    if data is None:
        data = {}

    if node is None:
        return data

    data[depth] = data.get(depth, [])
    data[depth].append(node.value)

    depth += 1
    get_depths(node.left, data, depth)
    get_depths(node.right, data, depth)
    return data


def average(nums):
    return reduce(lambda n, m: n + m, nums) / len(nums)


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node, value):
    if node:
        if value < node.value:
            node.left = insert(node.left, value)
        else:
            node.right = insert(node.right, value)

        return node

    else:
        return Node(value)
