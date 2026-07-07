class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_num = 0;
        while left < right:

            lesser = min(heights[right], heights[left])
            area = lesser * (right - left)
            if area > max_num:
                max_num = area

            if heights[right] == lesser:
                right -=1
            elif heights[left] == lesser:
                left +=1
        return max_num

