# LeetCode N78, Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(idx, res):
            if idx >= len(nums): # len(nums) = 3
                answer.append(res.copy())
                return
            
            # nums[idx]를 포함하는 경우
            res.append(nums[idx])
            dfs(idx+1, res)
            
            # 포함하지 않는 경우
            res.pop()
            dfs(idx+1, res)
        
        dfs(0, [])
        return answer