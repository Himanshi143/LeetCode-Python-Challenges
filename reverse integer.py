# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        if(x<0):
            c=int(a[1:][::-1])
            b=-c
        elif(x>0):
            b=int(a[::-1])
        if(len(str(x))==1):
            return x
        elif(b>=-2147483648 and b<=2147483647):
            if(x<0):
                return b
            elif(x>=0):
                return b
        else:
            return 0
        