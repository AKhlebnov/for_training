"""
14. Longest Common Prefix
"""


def long_pref(strs):
    min_str = min(strs, key=len)
    count = 0
    pref = ''
    for i in min_str:
        for j in strs:
            if j[count] != i:
                return pref

        pref += i
        count += 1
    return pref


lst = ['flower', 'flow', 'flight']


print(long_pref(lst))

# Write a function to find the longest common
# prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
