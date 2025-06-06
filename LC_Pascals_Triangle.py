class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        arr = [[1]*i for i in range(1, numRows + 1)]

        for i in range(2, len(arr)):
            for j in range(1, len(arr[i]) - 1):
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

        return arr



numRows = 5

sol = Solution()

print(sol.generate(numRows))


# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as show

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30