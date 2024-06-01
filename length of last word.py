#Given a string s consisting of words and spaces, return the length of the last word in the string.4
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=list(s.split())
        a=len(lst)
        return len(lst[a-1])
obj=Solution()
sol=obj.lengthOfLastWord(s="Hello             myself himanshi             ")
print("length of last word is: ",sol)