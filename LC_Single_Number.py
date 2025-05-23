class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

sol = Solution()

nums = [4,1,2,1,2]

print(sol.singleNumber(nums))


# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         count_dict = {num: 0 for num in nums}
#         for num in nums:
#             count_dict[num] += 1
#             if count_dict[num] == 2:
#                 count_dict.pop(num)
#         res = list(count_dict.keys())
#         return res[0]


# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         single_num = 0

#         for num in nums:
#             if nums.count(num) == 1:
#                 single_num = num
            
#         return single_num

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.