#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(list(s))
        b=sorted(list(t))
        c="".join(a)
        d="".join(b)
        return c==d
