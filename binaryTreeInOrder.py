

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Stack


def inorderTraversal(root):
    stack = []
    order = []

    if root == None:
        return []

    stack.append(root)

    while stack:
        element = stack.pop()
        if element.right != None:
            stack.append(element.right)
        if element.left != None:

            stack.append(element)

            stack.append(element.left)
            element.left = None
            element.right = None
        else:
            order.append(element.val)

    return order

# Recursion


def inorderTraversal1(root):
    result = []

    def recursion(root):
        if root.left is not None:
            recursion(root.left)
        if root.right is not None:
            recursion(root.right)
        result.append(root.val)

    if root is None:
        return result

    recursion(root)
    return result


root = TreeNode(3, TreeNode(1), TreeNode(2))
print(inorderTraversal(root))
