#Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if(len(nums)==1 or len(nums)==2):
            return nums.index(max(nums))
        for i in range(1,len(nums)-1):
            if(nums[i-1]<nums[i] and nums[i]>nums[i+1]):
                return i
            return nums.index(max(nums))    