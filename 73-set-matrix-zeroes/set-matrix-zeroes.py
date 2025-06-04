class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        # listi = []
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             listi.append((i,j))
        
        # for i,j in listi:
        #     for k in range(m):
        #         matrix[i][k] = 0
        #     for k in range(n):
        #         matrix[k][j]= 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0.1
                    for k in range(n):
                        if matrix[k][j] !=0:
                            matrix[k][j] = 0.1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0.1:
                    matrix[i][j] = 0

        