class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        n = len(height)
        p1 = 0
        p2 = n - 1
        total_water = 0
        while p1 <= p2:
            if height[p1] < height[p2]:

                total_water = max(total_water, (p2 - p1) * height[p1])
                p1 += 1
            else:
                
                total_water = max(total_water, (p2 - p1) * height[p2])
                p2 -= 1
        return total_water
        