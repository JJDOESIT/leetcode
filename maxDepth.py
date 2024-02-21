class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS


def maxDepth(root):
    if root is None:
        return 0

    left = 1 + maxDepth(root.left)
    right = 1 + maxDepth(root.right)
    return max(left, right)


n = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(maxDepth(n))
