class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

value = [1]
def constructBinaryTree(level):
    if level == 0:
        return
    node = Node()
    node.left = constructBinaryTree(level - 1)
    node.right = constructBinaryTree(level - 1)
    node.value = value[0]
    value[0] += 1
    return node

def findParent(node, target):
    if not node:
        return -1
    if node.left and node.right:
        if node.left.value == target or node.right.value == target:
            return node.value
    return max(findParent(node.left, target), findParent(node.right, target))

def solution(h, q):
    head = constructBinaryTree(h)
    res = []
    for item in q:
        res.append(findParent(head, item))

    return res
