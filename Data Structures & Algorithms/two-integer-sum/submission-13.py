class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen_list = {}

        for index, num in enumerate(nums):
            missing = target - num
            if missing in seen_list:
                return [seen_list[missing], index]
            seen_list[num] = index

            
            

            
        

        

            


                
        
        
            

        


