#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s=[]
        res=[]
        def backtrack(openN,closedN):
            if(openN==closedN==n):
                res.append("".join(s))
            if(openN<n):
                s.append("(")
                backtrack(openN+1,closedN)
                s.pop()
            if(closedN<openN):
                s.append(")")
                backtrack(openN,closedN+1)
                s.pop()
        backtrack(0,0)
        return res
        