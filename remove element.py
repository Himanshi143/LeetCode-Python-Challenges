#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        a=0
        for i in nums[0:]:
            if(i==val):
                a+=1
            else:
                continue
        for i in range(a):
            nums.remove(val)
        return len(nums)
obj=Solution()
sol=obj.removeElement(nums=[3,2,2,3],val=2)
print("Solution is: ",sol)