class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr)>1:
            maxi = max(arr[1:])
        else: 
            maxi = -1
        
        for i in range(len(arr)-1):
            if arr[i]>= maxi:
                maxi = max(arr[i+1:])
                arr[i] = maxi
            else:
                arr[i] = maxi

        arr[-1] = -1
        return arr