class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}
        for i in nums2:
            while stack and i > stack[-1]:
                greater[stack.pop()] = i
            stack.append(i)
        ans = []
        for i in nums1:
            ans.append(greater.get(i, -1))
        return ans
