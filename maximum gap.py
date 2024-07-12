#Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        if(len(nums)==1):
            return a
        else:
            for i in range(len(nums)-1):
                if(a<(nums[i+1]-nums[i])):
                    a=nums[i+1]-nums[i]
            print(a)
            return a
        