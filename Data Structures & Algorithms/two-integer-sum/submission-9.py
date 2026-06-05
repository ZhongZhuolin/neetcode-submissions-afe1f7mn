class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen_list = {}
        
        index = 0;
        for num in nums:
            missing = target - num
            if missing in seen_list:
                array = [seen_list[missing], index]
                return array
            seen_list[num] = index
            index += 1
            
            

            
        

        

            


                
        
        
            

        


