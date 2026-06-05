class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = {}
        sorted_array = []
        for word in strs:
            key = "".join(sorted(word))
            if key in sorted_list:
                sorted_list[key].append(word)
            else:
                sorted_list[key] = [word]
        return list(sorted_list.values())
            