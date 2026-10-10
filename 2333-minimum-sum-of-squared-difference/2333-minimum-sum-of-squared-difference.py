class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [0] * (10 ** 5 + 1)
        total_diff = 0
        k = k1 + k2
        mx = 0

        for x, y in zip(nums1, nums2):
            d = abs(x - y)
            diff[d] += 1
            total_diff += d
            mx = max(mx, d)

        if total_diff <= k:
            return 0
        
        for i in range(mx, 0, -1):
            if k == 0:
                break
            
            move = min(k, diff[i])
            diff[i] -= move
            diff[i - 1] += move
            k -= move
        
        ans = 0
        for i in range(mx + 1):
            ans += i * i * diff[i]

        return ans
