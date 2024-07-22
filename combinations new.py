class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        s=[]
        res=[]
        def backtrack(i):
            if(len(s)==k):
                res.append(s[:])
                return
            for j in range(i,n+1):
                s.append(j)
                backtrack(j+1)
                s.pop()
        backtrack(1)
        return res
