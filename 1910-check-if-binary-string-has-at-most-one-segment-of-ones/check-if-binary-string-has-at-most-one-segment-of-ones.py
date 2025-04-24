class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        counter = True
        boolie = True
        for i in range(len(s)):
            if s[i] == '1' and not boolie:
                return False
                break
            if s[i] == '1':
                counter = False
            elif s[i] == '0':
                boolie = False
            
        return True
            