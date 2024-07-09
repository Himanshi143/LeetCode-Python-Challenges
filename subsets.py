#Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        a.append([])
        for i in range(1,len(nums)+1):
            b=combinations(nums,i)
            c=[list(j) for j in b]
            a.extend(c)
            print(a)
        return a