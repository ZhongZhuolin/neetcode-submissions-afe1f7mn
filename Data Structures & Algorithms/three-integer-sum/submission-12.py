class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                new_target = 0 - nums[i]
                while right > left:
                    sums = nums[left] + nums[right]
                    if sums == new_target:
                        final_list.append((nums[i], nums[left], nums[right]))
                        left += 1
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
                    elif sums > new_target:
                        right -= 1
                    else:
                        left += 1
        return final_list



