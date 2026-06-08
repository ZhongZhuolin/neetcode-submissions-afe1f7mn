class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleans = "".join(filter(str.isalnum, s.lower()))
        right = len(cleans) - 1
        left = 0
        while right > left:
            if cleans[right] != cleans[left]:
                return False
            right -= 1
            left +=1
        return True