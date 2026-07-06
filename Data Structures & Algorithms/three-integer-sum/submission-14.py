class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = len(nums) - 1
            left = i + 1
            target = 0 - nums[i]
            while left < right:
                num_sum = nums[left] + nums[right]
                if num_sum > target:
                    right -= 1
                elif num_sum < target:
                    left += 1
                else:
                    final_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return final_list



