class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j = 0
        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                return True
                break
            j += 1
        return False