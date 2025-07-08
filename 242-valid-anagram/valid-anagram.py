class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        disc_1 = {}
        disc_2 = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in disc_1:
                disc_1[s[i]]+=1
            else:
                disc_1[s[i]] = 1
        for j in range(len(t)):
            if t[j] in disc_2:
                disc_2[t[j]]+=1
            else:
                disc_2[t[j]] = 1

        if disc_1 == disc_2:
            return True
        else:
            return False