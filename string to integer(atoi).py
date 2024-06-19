#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
#The algorithm for myAtoi(string s) is as follows:
#Whitespace: Ignore any leading whitespace (" ").
#Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
#Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
#Return the integer as the final result.
class Solution:
    def myAtoi(self, s: str) -> int:
        e=''
        p=''
        d=s.lstrip()
        if(d==""):
            return 0
        if(d[0]=="+" or d[0]=="-"):
            e=d[0]
            p=d[1:]
        else:
            e=''
            p=d[0:]
        print(p)
        a=''
        for i in p[0:]:
            if(ord(i)>=48 and ord(i)<=57):
                a+=i
            elif(ord(i)==43 or ord(i)==45):
                break
            elif(ord(i)==46 or ord(i)==32):
                break
            elif(ord(i)>=97 and ord(i)<=122):
                break
            else:
                continue
        print(a)
        if(a==''):
            return 0
        else:
            b=int(e+str(int(a)))
            if(b>=-2**31 and b<=(2**31)-1):
                return b
            elif(b<-2**31):
                return -2**31
            elif(b>(2**31)-1):
                return (2**31)-1

