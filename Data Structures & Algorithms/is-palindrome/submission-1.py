class Solution:
    def ifAlpha(self,c):
        return ('a' <= c <= 'z' or
                'A'<= c <= 'Z' or
                '0' <= c <='9')

    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1

        while left<right:
            while left<right and not self.ifAlpha(s[left]):
                left+=1
            while right>left and not self.ifAlpha(s[right]):
                right-=1
            if s[left].lower() !=s[right].lower():
                return False
            left+=1
            right-=1

        return True
        