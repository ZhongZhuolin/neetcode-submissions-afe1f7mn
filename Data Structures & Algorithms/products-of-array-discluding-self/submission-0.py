class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left side
        left = [1] * len(nums)
        for num in range(1, len(nums)):
                left[num] = left[num - 1] * nums[num - 1]

        #right side
        right = [1] * len(nums)
        for num in range(len(nums)-2, -1, -1):
                right[num] = right[num + 1] * nums[num + 1]
        #for each value
        array = []
        for num in range(len(nums)):
                array.append(left[num] * right[num])
        return array
        