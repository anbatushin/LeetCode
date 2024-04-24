class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_length = 0
        first_idx = 0

        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[first_idx])
                first_idx += 1
            max_length = max(max_length, i - first_idx + 1)
            chars.add(s[i])

        return max_length