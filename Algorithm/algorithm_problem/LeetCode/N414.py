# LeetCode 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

# 정수 배열 숫자가 주어지면 이 배열에서 세 번째 고유한 최대 숫자를 반환. 세 번째 최대값이 존재하지 않으면 최대값을 반환.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        
        if len(nums) < 3:
            return max(nums)
        
        return nums[2]


# 피드백
# O(n) 풀이법도 생각해 보는게 좋을 것 같다