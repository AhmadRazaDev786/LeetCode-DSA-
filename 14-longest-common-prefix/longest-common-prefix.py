class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        word = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(word) and word[j] == strs[i][j]:
                j+= 1
            word = word[:j]
            if word == "":
                return word
        return word
            