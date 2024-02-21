class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return node.left is None and node.right is None


def minDepth(root):
    if root is None or isLeaf(root):
        return 1

    if root.left is not None and root.right is not None:
        return min(1 + minDepth(root.left), 1 + minDepth(root.right))
    elif root.left is not None:
        return 1 + minDepth(root.left)
    else:
        return 1 + minDepth(root.right)


n = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
print(minDepth(n))
