class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total_water = 0
        leftmax = 0
        rightmax = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    total_water += leftmax - height[left]
                left += 1              
            else:
                if height[right] > rightmax:
                    rightmax = max(rightmax, height[right])
                else:
                    total_water += rightmax - height[right]
                right -= 1               
        return total_water    
