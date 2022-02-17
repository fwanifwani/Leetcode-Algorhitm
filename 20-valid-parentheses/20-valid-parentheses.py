class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = []

        result = True
        for i in s_list:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            elif len(stack) != 0:
                if (i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '(') or (
                        i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    result=False
                    break
            else:
                result=False
                break

        if len(stack) !=0:
            result=False

        return result