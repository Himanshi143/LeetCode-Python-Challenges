#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        arr=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]
                arr.append(s)
                if(s==target):
                    return target
                elif(s<target):
                    l+=1
                else:
                    r-=1
        print(arr)
        b=min(arr,key=lambda x:abs(x-target))
        return b
