class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digitSum = {}
        n = len(nums)
        for x in nums:
            s = 0
            ele = x
            while ele > 0:
                d = ele % 10
                s += d
                ele = ele // 10
            digitSum[x] = s

        def get_sort_key(x):
            return (digitSum[x], x)
        
        target = sorted(nums, key = get_sort_key)
        index = {value: i for i, value in enumerate(target)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or index[nums[i]] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index[nums[j]]
                cycle_size += 1
            
            swaps += cycle_size - 1
        return swaps
            