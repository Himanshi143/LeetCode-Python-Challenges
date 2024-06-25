#You are given an m x n integer matrix matrix with the following two properties:
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.
#You must write a solution in O(log(m * n)) time complexity.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        for i in matrix:
            for j in i:
                if(target==j):
                    print(j)
                    l=1
                    break
                else:
                    continue
        if(l==1):
            return True
        else:
            return False
        