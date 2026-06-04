class Solution:
    def twoSum(self, nums: List[int], target: int):
        l = {}
        array = []
        for num in range(len(nums)):
            l[num] = nums[num]
        left = 0
        while True:
            right = left + 1
            targ = target - l[left]
            for i in range(right, len(nums)):
                if l[i] == targ:
                    array.append(left)
                    array.append(i)
                    return array
            left += 1

            


                
        
        
            

        


