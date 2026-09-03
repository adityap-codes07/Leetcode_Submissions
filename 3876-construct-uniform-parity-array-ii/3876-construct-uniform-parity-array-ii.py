class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_element = float("inf")
        odd_count = 0
        for i in nums1:
            if i % 2 == 1:
                odd_count += 1
            min_element = min(min_element, i)
        return min_element % 2 == 1 or odd_count == 0

