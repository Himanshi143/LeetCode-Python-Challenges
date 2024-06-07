#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a1=[]
        z=p.count("*")
        for i in range(z,0,-1):
            t=p.replace("*"*i,"*")
            a1.append(t)
            print(i,t)
        a1.sort(key=len)
        if(len(a1)==0):
            a1.append(p)
        q=a1[0]
        f=re.fullmatch(q,s)
        print(f)
        if f:
            return True
        else:
            return False
        