class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        emptyarray = []
        i = 0
        while i< len(nums):
            if nums[i] in emptyarray:
                del nums[0:3]
                operations +=1
                emptyarray = []
                i = 0
                continue
            emptyarray.append(nums[i])
            i +=1
            

        return operations
        