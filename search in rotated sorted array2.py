#Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        a=0
        for i in nums:
            if(i==target):
                a+=1
                break
            else:
                continue
        if(a==1):
            return True
        else:
            return False
        