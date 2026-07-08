class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        if len(s) > 0:
            count = 1
        else:
            return 0
        max_length = count
        seen = {}
        seen[s[right]] = right
        while right < len(s) - 1:
            right += 1
            if s[right] in seen and seen[s[right]] >= left:
                count = right - seen[s[right]]
                left = seen[s[right]] + 1
                seen[s[right]] = right
            else:
                count += 1
                seen[s[right]] = right
            if count > max_length:
                    max_length = count
        return max_length

            
                
