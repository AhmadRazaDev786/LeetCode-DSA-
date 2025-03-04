class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        while 3**(i+1) <= n:
            i+=1

        while i>=0:
            if 3**i<=n:
                n = n -3**i
            i-=1
        return n==0