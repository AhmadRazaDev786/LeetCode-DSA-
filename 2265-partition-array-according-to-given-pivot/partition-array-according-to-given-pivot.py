class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []
        i = 0
        while i < len(nums):
            if nums[i]< pivot:
                left.append(nums[i])
            elif nums[i] == pivot:
                middle.append(nums[i])
            else:
                right.append(nums[i])
            i+=1
        nums[:] = left + middle + right
        return nums