class Solution:
    def twoSum(self, nums: List[int], target: int):
        li = {}
        
        i = 0;
        for num in nums:
            sub = target - num
            if sub in li:
                array = [li[sub], i]
                return array
            li[num] = i
            i += 1
            
            

            
        

        

            


                
        
        
            

        


