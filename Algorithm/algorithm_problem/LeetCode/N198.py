'''
LeetCode 198. House Robber
https://leetcode.com/problems/house-robber/description/

어느 집에서든 돈을 훔쳐올 수 있지만 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능하다. 
훔칠 수 있는 가장 큰 금액을 출력하라.

전형적인 DP 문제
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i]) # [2,1,1,2] case
        
        return max(dp)