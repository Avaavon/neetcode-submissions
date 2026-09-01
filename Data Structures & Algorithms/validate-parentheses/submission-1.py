
#traverse thru each char add to stack, but
#if its closed 
#then check if the topmost char in 'stack' matches

class Solution:
    def isValid(self, s: str) -> bool:
        #create empty stack to add open parentheses
        stack=[]
        #create a dict for closed parentheses: open parentheses
        closetoopen={
        '}':'{',
        ']':'[',
        ')':'('
        }

        for char in s:
            if char in closetoopen:
                if stack and closetoopen[char]==stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return not stack
            
                

