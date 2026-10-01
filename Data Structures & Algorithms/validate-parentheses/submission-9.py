class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_set = {")":"(", "]":"[", "}":"{"}

        if len(s) == 1:
            return False

        for c in s:
            if c in p_set and stack and stack[-1] == p_set[c]:
                stack.pop()
            elif c in p_set.values():
                stack.append(c)
            else:
                return False
        return len(stack) == 0
