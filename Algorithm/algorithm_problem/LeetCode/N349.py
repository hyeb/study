# LeetCode 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

# 두 배열의 교집합 구하기

# binary search로 풀진 못하고 그냥 바로 간단하게 set으로 ...ㅎ
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:           
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return nums1 & nums2