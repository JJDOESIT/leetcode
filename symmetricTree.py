class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS


def isSymmetric(root):
    def dfs(a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        return dfs(a.left, b.right) and dfs(a.right, b.left)

    return dfs(root.left, root.right)


n = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
             TreeNode(2, TreeNode(3), TreeNode(4)))

print(isSymmetric(n))
