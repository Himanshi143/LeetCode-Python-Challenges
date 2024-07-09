#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a=[]
        a.append([])
        for i in range(1,len(nums)+1):
            b=combinations(nums,i)
            d=[sorted(list(k)) for k in b]
            e={tuple(z) for z in d}
            f=[list(m) for m in e]
            a.extend(f)
            print(a)
        return a