#Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        a=[]
        if(len(s)==1):
            return s
        for i in range(len(s)):
            b=""
            b+=s[i]
            a.append(b)
            for j in s[i+1:]:
                b+=j
                a.append(b)
        a.sort(key=len,reverse=True)
        for k in a[0:]:
            l=k[::-1]
            if(k==l):
                return k

