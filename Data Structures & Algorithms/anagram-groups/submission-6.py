class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            freq_list = {}
            key = [0] * 26

            for letter in word:
                if int(ord(letter) - ord("a")) in freq_list:
                    freq_list[int(ord(letter) - ord("a"))] += 1
                else:
                    freq_list[int(ord(letter) - ord("a"))] = 1

            new_key = []
            for index, frequency in enumerate(key):
                if index in freq_list:
                    frequency = freq_list[index]
                new_key.append(frequency)

            if tuple(new_key) in anagram_dict:
                anagram_dict[tuple(new_key)].append(word)
            else:
                anagram_dict[tuple(new_key)] = [word]

        return list(anagram_dict.values())


            
                    
                
                 
                    