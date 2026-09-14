class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen = 1
        for i in range(len(s)):
            seen = {s[i]}
            curr = 1
            for j in range(i + 1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    curr += 1
                else:
                    break
                maxlen = max(maxlen, curr)
        return maxlen
            
