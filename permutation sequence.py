#The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#By listing and labeling all of the permutations in order, we get the following sequence 
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        per=permutations([str(x) for x in range(1,n+1)])
        p=["".join(i) for i in per]
        return p[k-1]