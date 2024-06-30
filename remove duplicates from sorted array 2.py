#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        d=Counter(nums)
        for i in d:
            print('d',d[i])
            if(d[i]<=2):
                a+=d[i]
            else:
                a+=2
                for j in range(d[i]-2):
                    nums.remove(i)
            print(nums)
            print(a)
        return a
        