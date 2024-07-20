#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]
                if(s==0):
                    if([nums[i],nums[l],nums[r]] not in arr):
                        arr.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif(s<0):
                    l+=1
                else:
                    r-=1
        return arr