class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            search_num = target - num                
            if search_num in seen:
                return[seen[search_num], i]
            else:
                seen[num] = i
