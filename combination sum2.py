#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        s=[]
        res=[]
        def backtrack(i,currs):
            if(currs==target):
                if(s not in res):
                    res.append(s[:])
                return
            if(currs>target or i>=len(candidates)):
                return
            s.append(candidates[i])
            backtrack(i+1,currs+candidates[i])
            s.pop()
            backtrack(i+1,currs)
        backtrack(0,0)
        return res