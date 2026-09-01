"""
check from rows then 
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        least_row = 0
        greatest_row = rows - 1

        while least_row <= greatest_row:
            mid_row = (least_row + greatest_row) // 2
            
            # if target is > mid_row greatest
            if target > matrix[mid_row][-1]:
                least_row = mid_row + 1

            # if target is < mid_row least
            elif target < matrix[mid_row][0]:
                greatest_row = mid_row - 1
            
            else:
                break
            
        if not (least_row <= greatest_row):
            return False
        
        row = (least_row + greatest_row) // 2

        l = 0
        r = cols - 1

        while l<=r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False






