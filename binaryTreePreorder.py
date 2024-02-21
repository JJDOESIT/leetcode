class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion


def preorderTraversal(root):
    order = []

    def recursion(node):
        if node:
            order.append(node.val)
            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)

    recursion(root)
    return order


n = TreeNode(1, None, TreeNode(2, TreeNode(3)))

print(preorderTraversal(n))
