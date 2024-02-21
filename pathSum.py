class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# DFS


def hasPathSum(root, targetSum):
    def isLeaf(node):
        return node.left is None and node.right is None

    def dfs(node, target, sum):
        if node is None:
            return False

        if node.val + sum == target and isLeaf(node):
            return True
        return dfs(node.left, target, sum + node.val) or dfs(node.right, target, sum + node.val)

    if root is None:
        return False

    if root.val == targetSum and isLeaf(root):
        return True

    if root.val == targetSum and isLeaf(root):
        return False

    return dfs(root, targetSum, 0)


n = TreeNode(0, )
print(hasPathSum(n, 1))
