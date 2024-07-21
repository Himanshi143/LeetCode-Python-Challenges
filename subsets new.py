from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[]
        res=[]
        def backtrack(i):
            if(i==len(nums)):
                res.append(s[:])
                return
            s.append(nums[i])
            backtrack(i+1)
            s.pop()
            backtrack(i+1)
        backtrack(0)
        return res
