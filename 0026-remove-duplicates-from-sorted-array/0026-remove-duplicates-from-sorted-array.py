class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, i, n = 0, 1, len(nums)
        while i < n:
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
            i += 1
        return k + 1
            


        