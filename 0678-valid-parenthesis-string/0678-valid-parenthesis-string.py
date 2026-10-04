class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []
        for i, paren in enumerate(s):
            if paren == "(":
                openStack.append(i)
            elif paren == "*":
                starStack.append(i)
            else:
                if len(openStack) > 0:
                    openStack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
                else:
                    return False
        while openStack and starStack:
            if openStack.pop() > starStack.pop():
                return False
        return len(openStack) == 0

