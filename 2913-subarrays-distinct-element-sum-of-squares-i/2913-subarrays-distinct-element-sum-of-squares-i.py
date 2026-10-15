class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            res = []
            for j in range(i, len(nums)):
                res = nums[i: j + 1]
                seen = {}
                cnt = 0
                for x in range(len(res)):
                    if res[x] not in seen:
                        seen[res[x]] = x
                        cnt += 1                 
                ans += cnt * cnt
        return ans
        