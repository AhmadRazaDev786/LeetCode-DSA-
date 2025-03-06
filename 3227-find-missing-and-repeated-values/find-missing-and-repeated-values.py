from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]  
        disc = defaultdict(int)
        n = len(grid) 
        total_numbers = n * n  
        
        for row in grid:
            for num in row:
                disc[num] += 1
        
        # repeated
        for num, count in disc.items(): 
            if count == 2:
                ans[0] = num 
                break 
        
        #missing
        for num in range(1, total_numbers + 1):
            if disc[num] == 0: 
                ans[1] = num 
                break  
        
        return ans
