class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        max_length = 0
        first_index = 0

        for i in range(len(s)):
            if s[i] in chars:
                first_index = max(first_index, chars[s[i]] + 1)
            max_length = max(max_length, i - first_index + 1)
            chars[s[i]] = i

        return max_length