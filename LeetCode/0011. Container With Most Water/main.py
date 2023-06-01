class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea, area, minHeight, left = 0, 0, 0, 0
        right = len(height) - 1
        
        while left < right:
            if height[left] < height[right]:
                minHeight = height[left]
            else:
                minHeight = height[right]

            width = (right - left)
            area = minHeight * width
            
            if area > maxArea:
                maxArea = area

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return maxArea

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

solution = Solution()
max_area = solution.maxArea(height)
print("Max amount of water:", max_area) # Max amount of water: 49