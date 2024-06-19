#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[]
        p=0
        for i in nums[0:]:
            if(i==target):
                a.append(p)
            p+=1
        if(a==[]):
            return [-1,-1]
        elif(len(a)==1):
            a.append(a[0])
        elif(len(a)>2):
            z=len(a)
            b=[a[0],a[z-1]]
            return b
        return a
