class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPal(left, right - 1) or isPal(left + 1, right)
            else:
                left += 1
                right -= 1
        return True