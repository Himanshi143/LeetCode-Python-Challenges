class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        a=0
        for i in range(len(s)-1):
            if(d[s[i]]==d[s[i+1]]):
                a+=d[s[i]]
            elif(d[s[i]]>d[s[i+1]]):
                a+=d[s[i]]
            elif(d[s[i]]<d[s[i+1]]):
                a-=d[s[i]]
        a+=d[s[len(s)-1]]
        return a
l=Solution()
s=str(input("Enter roman: "))
ans=l.romanToInt(s)
print("Integer value t0 ",s,"is: ",ans)