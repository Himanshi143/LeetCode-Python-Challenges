#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=''
        c=''
        for i in range(len(strs[0])):
            a+=strs[0][i]
            b=[]
            for j in range(len(strs)):
                b.append(a in strs[j][0:i+1])
                print(a)
            if(all(b)==True):
                c+=strs[0][i]
                continue
            else:
                break
        print(a)
        print(c)
        return c