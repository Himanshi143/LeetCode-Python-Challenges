#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        p=combinations(range(1,n+1),k)
        q=list(list(i) for i in p)
        print(q)
        return q