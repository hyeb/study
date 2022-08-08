# LeetCode N39, Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def dfs(idx, res):
            if sum(res) == target:
                answer.append(res.copy())
                return
            if sum(res) > target:
                return
            
            for i in range(idx, len(candidates)):
                res.append(candidates[i])
                dfs(i, res)
                res.pop()
                
        dfs(0, [])
        return answer