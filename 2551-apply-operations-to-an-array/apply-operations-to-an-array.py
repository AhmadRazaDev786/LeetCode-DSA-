class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(1,len(nums)):
            if nums[left] == nums[right]:
                nums[left], nums[right] = nums[left]*2, 0
            left+=1
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums