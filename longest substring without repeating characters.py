#Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        a=[]
        if(len(s)==1):
            return 1
        for i in range(len(s)):
            b=""
            b+=s[i]
            for j in s[i+1:]:
                if j in b:
                    a.append(b)
                    break
                elif j not in b:
                    b+=j
            if b not in a:
                a.append(b)
        print(a)
        zz=0
        for k in a[0:]:
            if(zz<=len(k)):
                zz=len(k)
            else:
                continue
        return zz
