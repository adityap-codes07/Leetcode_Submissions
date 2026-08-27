class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        n = len(arr)
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        if i == n - 1 or i == 0:
            return False
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        return True if i == n - 1 else False