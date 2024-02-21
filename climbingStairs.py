
# Dynamic programming
class Solution:
    def climbStairs(self, n: int):
        memo = {}
        memo[1] = 1
        memo[2] = 2

        return self.climb(n, memo)

    def climb(self, n, memo):
        if (n in memo):
            return memo[n]

        memo[n] = self.climb(n - 1) + self.climb(n - 2)
        return memo[n]
