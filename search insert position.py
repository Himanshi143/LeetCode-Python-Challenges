class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            print(nums[i])
            if(nums[i]==target):
                return i
            else:
                if(target<nums[0]):
                    return 0
                elif(target>nums[len(nums)-1]):
                    return len(nums)
                elif(target>nums[i] and target<nums[i+1]):
                    return i+1
                else:
                    continue
obj=Solution()
ans=obj.searchInsert(nums=[1,3,4,6],target=5)
print("ans: ",ans)