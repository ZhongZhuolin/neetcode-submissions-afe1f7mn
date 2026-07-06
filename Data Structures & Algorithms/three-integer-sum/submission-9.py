class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_set = set()
        final_list = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                new_target = 0 - nums[i]
                while right > left:
                    sums = nums[left] + nums[right]
                    if sums == new_target:
                        
                        list_set.add((nums[i], nums[left], nums[right]))
                        right -= 1
                        left += 1
                    elif sums > new_target:
                        right -= 1
                    else:
                        left += 1
        for i in list_set:
            final_list. append(i)
        return final_list



