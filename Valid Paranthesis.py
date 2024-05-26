class Solution:
    def isValid(self, s: str) -> bool:
        d={"(":")","{":"}","[":"]"}
        l=[]
        for i in s:
            if i in d:
                l.append(i)
            elif(d[l.pop()]!=i or len(l)==0):
                return False
        return len(l)==0
ss=Solution()
s=str(input("Enter str: "))
ans=ss.isValid(s)
print(ans)
