#Given an array nums of size n, return the majority element.
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=dict(Counter(nums))
        print(d)
        val=max(d.values())
        key=[i for i in d if d[i]==val]
        print(key)
        return key[0]
        