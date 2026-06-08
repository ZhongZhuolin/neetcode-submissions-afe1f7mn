class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecdict = {}
        consecutive = []
        numse = sorted(set(nums))
        most = 0
        for i, num in enumerate(numse):
                if i != 0:
                        if (numse[i - 1] + 1) == numse[i]:
                                consecutive.append(num)
                        else:
                                most = max(most, len(consecutive))
                                consecutive = [num]

                else:
                        consecutive.append(num)
        most = max(most, len(consecutive))
        return most


                
                


