#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a=[]
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if(len(digits)<=0 and len(digits)>4):
            return a
        elif(len(digits)==1):
            return list(d[int(digits[0])])
        elif(len(digits)==2):
            p=list(d[int(digits[0])])
            q=list(d[int(digits[1])])
            for i in p[0:]:
                for j in q[0:]:
                    z=i+j
                    a.append(z)
            return a
        elif(len(digits)==3):
            p=list(d[int(digits[0])])
            q=list(d[int(digits[1])])
            r=list(d[int(digits[2])])
            for i in p[0:]:
                for j in q[0:]:
                    for k in r[0:]:
                        z=i+j+k
                        a.append(z)
            return a
        elif(len(digits)==4):
            p=list(d[int(digits[0])])
            q=list(d[int(digits[1])])
            r=list(d[int(digits[2])])
            s=list(d[int(digits[3])])
            for i in p[0:]:
                for j in q[0:]:
                    for k in r[0:]:
                        for l in s[0:]:
                            z=i+j+k+l
                            a.append(z)
            return a
        else:
            return a