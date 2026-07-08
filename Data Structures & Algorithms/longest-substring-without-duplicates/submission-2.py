class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        if len(s) > 0:
            count = 1
        else:
            return 0
        max_length = count
        seen = set()
        while right < len(s)-1:
            seen.add(s[right])
            right += 1
            if s[right] in seen:
                count = 1
                seen.clear()
                left += 1
                right = left
            else:
                count += 1
                if count > max_length:
                    max_length = count
        return max_length

            
                
