class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        c= 0
        a = 1
        b = 1
        for i in range(n-2, -1, -1):
            c = a + b
            a = b
            b = c

        return c

        
