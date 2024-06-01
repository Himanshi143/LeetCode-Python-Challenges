#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
obj=Solution()
haystack="Himanshi"
needle="an"
sol=obj.strStr(haystack,needle)
print("Index of ",needle,"in ",haystack,"is: ",sol)