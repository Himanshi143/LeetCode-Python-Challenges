#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            w="".join(sorted(i))
            if w in d:
                d[w].append(i)
            else:
                d[w]=[i]
        print(d)
        return d.values()
