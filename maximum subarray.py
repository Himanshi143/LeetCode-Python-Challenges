#Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-sys.maxsize-1
        sum=0
        for i in nums:
            sum+=i
            if(sum>maxi):
                maxi=sum
            if(sum<0):
                sum=0
        return maxi