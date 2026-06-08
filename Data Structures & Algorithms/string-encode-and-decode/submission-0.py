class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
                result = result + str(len(word)) + "#" + word
        return result
    def decode(self, s: str) -> List[str]:
        word_list = []
        i = 0
        while i < len(s):
                string = ""
                num = ""
                newnum = 0
                while s[i] != "#":
                        num += s[i]
                        i += 1
                        newnum = int(num)
                for num in range(i + 1, newnum + 1 + i):
                        string += s[num]
                i += newnum + 1
                word_list.append(string)
        return word_list
