class Solution:
    def twoSum(self, nums: List[int], target: int):
        l = {}
        
        i = 0;
        for num in nums:
            sub = target - num
            if sub in l:
                array = [l[sub], i]
                return array
            l[num] = i
            i += 1
            

            
        

        

            


                
        
        
            

        


