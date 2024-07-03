#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        p=permutations(nums,l)
        per=set(i for i in p)
        lst=list(list(j) for j in per)
        print(lst)
        return lst