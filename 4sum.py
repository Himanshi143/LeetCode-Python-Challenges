#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#0 <= a, b, c, d < n
#a, b, c, and d are distinct.
#nums[a] + nums[b] + nums[c] + nums[d] == target

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while(l<r):
                    s=nums[i]+nums[j]+nums[l]+nums[r]
                    if(s==target):
                        if([nums[i],nums[j],nums[l],nums[r]] not in arr):
                            arr.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                    elif(s<target):
                        l+=1
                    else:
                        r-=1
        print(arr)
        return arr