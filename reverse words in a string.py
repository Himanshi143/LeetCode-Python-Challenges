#Given an input string s, reverse the order of the words.
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        d=list(s.split())
        return " ".join(d[::-1])

        