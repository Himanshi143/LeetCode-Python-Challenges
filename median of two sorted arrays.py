#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
import statistics as s
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        print(nums1)
        return s.median(nums1)