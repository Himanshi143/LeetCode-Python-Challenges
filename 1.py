#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
s=Solution()
print(s.twoSum(nums=[1,3,45,12,6],target=9))