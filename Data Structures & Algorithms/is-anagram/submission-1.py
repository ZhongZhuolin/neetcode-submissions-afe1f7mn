class Solution:
    def count_freq(self, String):
        freq_list = {}
        for char in String:
            if char in freq_list:
                freq_list[char] += 1
            else:
                freq_list[char] = 1
        return freq_list
        
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_freq(s) == self.count_freq(t)

