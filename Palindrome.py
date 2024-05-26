#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        a=list(x)
        a.reverse()
        b="".join(a)
        if x==b:
            return True
        else:
            return False
s=Solution()
print(s.isPalindrome(x=-121))
