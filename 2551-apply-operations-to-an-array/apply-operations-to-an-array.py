class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        non_zero = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[non_zero], nums[j] = nums[j], nums[non_zero]
                non_zero +=1
        return nums