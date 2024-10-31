"""
67. Add Binary.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


a = "1010"
b = "1011"
sol = Solution()
print(sol.addBinary(a, b))

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# Решение с перебором строк:

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = a.zfill(max(len(a), len(b)))
#         b = b.zfill(max(len(a), len(b)))
#         carry = 0
#         res = ''
        
#         for i in range(len(a) - 1, -1, -1):
#             sum_bits = int(a[i]) + int(b[i]) + carry
            
#             if sum_bits == 0:
#                 res = '0' + res
#                 carry = 0
#             elif sum_bits == 1:
#                 res = '1' + res
#                 carry = 0
#             elif sum_bits == 2:
#                 res = '0' + res
#                 carry = 1
#             elif sum_bits == 3:
#                 res = '1' + res
#                 carry = 1

#         if carry == 1:
#             res = '1' + res

#         return res

# Аналогичное решение, но немного другая логика:

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = a.zfill(max(len(a), len(b)))
#         b = b.zfill(max(len(a), len(b)))
#         carry = False
#         res = ''

#         for i in range(len(a)-1, -1, -1):

#             if a[i] == '0' and b[i] == '0':
#                 if carry:
#                     res = '1' + res
#                     carry = False
#                 else:
#                     res = '0' + res

#             elif (
#                 (a[i] == '1' and b[i] == '0') or
#                 (a[i] == '0' and b[i] == '1')
#             ):
#                 if carry:
#                     res = '0' + res
#                 else:
#                     res = '1' + res

#             elif a[i] == '1' and b[i] == '1':
#                 if carry:
#                     res = '1' + res
#                 else:
#                     res = '0' + res
#                 carry = True

#         if carry:
#             res = '1' + res

#         return res