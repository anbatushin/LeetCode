class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        max_length = 0
        freq = 0
        left = 0

        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
            freq = max(freq, chars[s[i]])
            if i - left + 1 - freq > k:
                chars[s[left]] -= 1
                left += 1
            max_length = i - left + 1

        return max_length