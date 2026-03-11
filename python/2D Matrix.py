class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row,col=len(matrix),len(matrix[0])
        left,right=0,row*col-1
        while left<=right:
            mid=(left+right)//2
            r=mid//col
            c=mid%col
            midv=matrix[r][c]
            if midv==target:
                return True
            elif midv<target:
                left=mid+1
            else:
                right=mid-1
        return False
