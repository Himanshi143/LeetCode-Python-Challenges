class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2==0):
            l=[]
            p=[]
            for i in s[0:]:
                if(i=="(" or i=="{" or i=="["):
                    l.extend(i)
                    print(l)
                else:
                    p.extend(i)
                    if(i==")" and l[-1]=="("):
                        l.pop()
                        p.pop()
                    elif(i=="}" and l[-1]=="{"):
                        l.pop()
                        p.pop()
                    elif(i=="]" and l[-1]=="["):
                        l.pop()
                        p.pop()
                    else:
                        return False
                        break
            if len(l)==0 and len(l)==len(p):
                return True
            else:
                return False
        else:
            return False
ss=Solution()
s=str(input("Enter string: "))
ans=ss.isValid(s)   
print("Is ",s,"is valid: ",ans) 