class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                stack.append(letter)
            else:
                if stack and letter == dict.get(stack[-1]):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
