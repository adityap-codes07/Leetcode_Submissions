class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            maxlen = max(maxlen, i - left + 1)
        return maxlen