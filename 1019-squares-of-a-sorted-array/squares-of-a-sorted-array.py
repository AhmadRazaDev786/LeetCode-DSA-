class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        pointer = -1
        returner = len(nums)*[0]
        while left<=right:
            if nums[left]*nums[left] > nums[right]*nums[right]:
                returner[pointer] = nums[left]*nums[left]
                left +=1
            else:
                returner[pointer] = nums[right]*nums[right]
                right -=1
            pointer -=1
        return returner