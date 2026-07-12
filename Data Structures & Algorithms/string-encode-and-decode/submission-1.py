class Solution:

    def encode(self, strs: List[str]) -> str:
        word_string = ""
        for word in strs:
            word_string += str(len(word)) + "#" + word
        return word_string
    # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        left = 0
        count = ""
        list_words = []
        while left < len(s):
            if s[left] != "#":
                count += str(s[left])
                left += 1

            else:
                left += 1
                word = ""
                for letter in range(int(count) ):
                    word += str(s[left])
                    left += 1
                list_words.append(word)
                word = ""
                count = ""
        return list_words
                





        
        
                    

            

        
            
        






