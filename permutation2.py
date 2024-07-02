#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per=permutations(nums)
        p=set(i for i in per)
        q=list(list(j) for j in p)
        return q