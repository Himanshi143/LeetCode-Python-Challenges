#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        if(len(nums)<=2):
            return a
        else:
            for i in range(len(nums)):
                b=[]
                b.append(nums[i])
                for j in range(i+1,len(nums)):
                    c=[]
                    c.append(nums[j])
                    for k in nums[j+1:]:
                        if(b[0]+c[0]+k==0):
                            b.extend(c)
                            b.append(k)
                            a.append(b)
                            del(b)
                            b=[]
                            b.append(nums[i])
                        else:
                            continue 
            for z in a[0:]:
                z.sort()
                if(a.count(z)>1):
                    a.remove(z)
            return a
