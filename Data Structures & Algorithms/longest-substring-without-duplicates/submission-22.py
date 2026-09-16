class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return 1
        else:
            right = 0
            left = 0
            largest = 0
            seen = {}
            while right <= len(s) - 1:
                if s[right] not in seen:
                    seen[s[right]] = right
                    newlargest = right - left + 1
                    if newlargest > largest:
                        largest = newlargest
                else:
                    if seen[s[right]] >= left:
                        left = seen[s[right]] + 1
                    seen[s[right]] = right
                    newlargest = right - left + 1
                    if newlargest > largest:
                        largest = newlargest

                right += 1
            return largest

                
 

                
                

