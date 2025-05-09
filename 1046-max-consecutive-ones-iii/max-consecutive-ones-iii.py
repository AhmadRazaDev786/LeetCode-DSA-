class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length, maxlength, zeros_count = 0, 0, 0
        left=0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count +=1
            if zeros_count>k:
                while nums[left]!=0:
                    left+=1
                left+=1
                zeros_count-=1
            length = right-left+1
            maxlength= max(maxlength, length)
        return maxlength