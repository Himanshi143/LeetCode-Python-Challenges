#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        b=nums[0]
        for i in nums[1:]:
            if(b==i):
                nums.remove(i)
            else:
                b=i
        return len(nums)
obj=Solution()
ans=obj.removeDuplicates(nums=[0,0,1,1,2,2,2,3,3,3,4,4,4,4,4,5])
print("Sol is: ",ans)