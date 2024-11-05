"""
70. Climbing Stairs.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        elif n == 2:
            return 2

        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1


n = 10
sol = Solution()
print(sol.climbStairs(n))


# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:

# 1 <= n <= 45
