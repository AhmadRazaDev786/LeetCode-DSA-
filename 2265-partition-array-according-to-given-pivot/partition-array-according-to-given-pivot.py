class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        middle = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i]) 
            elif nums[i] == pivot:
                middle.append(nums[i]) 

            else:
                right.append(nums[i])  

        nums[:] = left + middle + right
        return nums