class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        boolie = True
        for i in range(len(s)):
            if s[i] == '1' and not boolie:
                return False
                break
            if s[i] == '0':
                boolie = False
            
        return True
            