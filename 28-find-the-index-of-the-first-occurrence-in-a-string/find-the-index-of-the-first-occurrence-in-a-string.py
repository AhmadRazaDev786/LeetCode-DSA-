class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first = 0
        second = 0
        i = 0
        while i < len(haystack) and first< len(needle):
            if haystack[i] == needle[first]:
                if first == 0:
                    second = i
                first += 1
                if first == len(needle):
                    return second
            else:
                if first > 0:
                    i = second
                first = 0
            i +=1
        
        return -1