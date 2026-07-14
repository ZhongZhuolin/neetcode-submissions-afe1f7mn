class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target <= nums[left]:
            return left
        elif target > nums[right]:
            return right + 1
        elif target == nums[right]:
            return right
        else:
            while right > left:
                middle = int((right - left/2)) + left
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
        return right + 1



