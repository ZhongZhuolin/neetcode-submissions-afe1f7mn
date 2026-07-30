class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        prev_list = []
        for x in range(rowIndex + 1):
            if not prev_list:
                prev_list = [1]           
            else:
                new_list = []
                length = len(prev_list)
                for i in range(length + 1):
                    if i == 0 or i == length:
                        new_list.append(1)
                    else:
                        new_list.append(prev_list[i - 1] + prev_list[i])
                    
                prev_list = new_list
            
        return prev_list

