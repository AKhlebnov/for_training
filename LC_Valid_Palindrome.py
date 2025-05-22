class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        return filtered == filtered[::-1]


sol = Solution()

s = 'A man, a plan, a canal: Panama'

print(sol.isPalindrome(s))