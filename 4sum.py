class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a={tuple(sorted((nums[i],nums[j],nums[k],nums[l]))) for i in range(len(nums)) for j in range(i+1,len(nums)) for k in range(j+1,len(nums)) for l in range(k+1,len(nums)) if nums[i]+nums[j]+nums[k]+nums[l]==target}
        print(a)
        e=[list(o) for o in a]
        return e