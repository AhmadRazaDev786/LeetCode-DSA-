class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # disc = defaultdict(int)
        # for i in magazine:
        #     disc[i] +=1
        
        # for j in ransomNote:
        #     if disc[j] >0:
        #         disc[j]-=1
        #     else:
        #         return False
        # return True

        count_ransomNote = Counter(ransomNote)
        count_magzine = Counter(magazine)

        for char, count in count_ransomNote.items():
            if count_magzine[char] < count:
                return False
        return True