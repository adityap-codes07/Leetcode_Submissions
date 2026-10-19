class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        start = l
        res = []
        while start < n and nums[start] == target:
            res.append(start)
            start += 1
        return res
