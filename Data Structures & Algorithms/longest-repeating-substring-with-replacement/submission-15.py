class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        freqs = {}
        max_freq = 0

        for right in range(len(s)):
            c = s[right]
            freqs[c] = freqs.get(c, 0) + 1
            window = (right - left) + 1
            max_freq = max(freqs[c], max_freq)

            if window - max_freq > k:
                freqs[s[left]] -= 1
                left += 1
                window -= 1

            max_count = max(max_count, window)
        return max_count

            


       



                

                    
                


