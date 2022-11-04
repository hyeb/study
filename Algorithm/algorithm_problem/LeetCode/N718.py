# Leetcode 718. Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

'''
두 개의 정수 배열 nums1과 nums2가 주어지면 두 배열에 모두 나타나는 부분 배열의 최대 길이를 반환
hint1: Use dynamic programming.

- nums1과 nums2에서 size만큼 잘라서 가져와서 비교  
- 잘라서 가져온 window가 서로 같다면 기존 res 값과 len(window)을 비교해서 더 큰값으로 업데이트
- size길이가 max(len(nums1), len(nums2))에 도달했을 때 break
'''

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        len1, len2 = len(nums1), len(nums2)
        dp = [[0] * (len2+1) for _ in range(len1+1)] # 비교대상인 nums2를 기준으로
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
            res = max(res, max(dp[i]))
        
        return res

# accept 되긴 하지만 시간이 오래 걸림.
# 더 효율적인 방법이 있는지 생각해보기.