class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen_list = {}

        for index, num in enumerate(nums):
            missing_num = target - num
            if missing_num in seen_list:
                array = [seen_list[missing_num], index]
                return array
            seen_list[num] = index
            
            

            
        

        

            


                
        
        
            

        


