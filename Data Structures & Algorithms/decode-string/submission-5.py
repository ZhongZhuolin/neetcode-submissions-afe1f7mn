class Solution:
    def decodeString(self, s: str) -> str:
        string = ""
        stack = []
        for item in s:
            if item != "]":
                stack.append(item)
            else:
                while stack[-1] != "[":
                    string = stack.pop() + string
                if stack[-1] == "[":
                    stack.pop()
                k = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    k = str(stack.pop()) + k
                if int(k) > 0:
                    string = string * int(k)
                    for letter in string:
                        stack.append(letter)
                    string = ""
        return "".join(stack)




