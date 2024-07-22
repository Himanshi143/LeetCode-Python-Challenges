#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        s=[]
        res=[]
        def backtrack(i,currs):
            if(currs==target):
                res.append(s[:])
                return
            if(currs>target or i>=len(candidates)):
                return
            s.append(candidates[i])
            backtrack(i,currs+candidates[i])
            s.pop()
            backtrack(i+1,currs)
        backtrack(0,0)
        return res