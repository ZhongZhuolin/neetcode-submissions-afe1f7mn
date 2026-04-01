class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openclose = {")" : "(", "}":"{" , "]":"["}
        
        for c in s:
            if c in openclose and stack:
                if openclose[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                    stack.append(c)
        if len(stack) <1:
            return True
        return False
            


