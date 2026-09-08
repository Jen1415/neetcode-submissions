class Solution:
    @classmethod
    def isValid(self, s: str) -> bool:
        myDict = {'(': ')',
                  '{': '}', 
                  '[': ']'}
        stack = []
        for bracket in s:
            if bracket in myDict.keys():
                stack.append(bracket)   
            elif bracket in myDict.values():
                if len(stack) == 0:
                    return False
                open = stack.pop()
                if myDict[open] != bracket:
                    return False
        return len(stack) == 0        