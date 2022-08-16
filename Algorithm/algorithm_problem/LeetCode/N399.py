# LeetCode 399, Evaluate division
# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(list)
        visited = [False] * (n+1)

        for i in range(len(values)):
            A, B = equations[i]
            dic[A].append(([values[i]], [B]))
            dic[B].append(([1/values[i]], [A]))
        
        def dfs(visited, A, B, num):
            if A not in dic or B not in dic:
                return -1.0
            if A == B:
                return num

            visited.add(A)

            idx = 0
            for _, e in dic[A]:
                if e == B:
                    break
                idx += 1
            new, node = dic[A][idx]
            num *= new
            if node not in visited:
                dfs(node, B, num)           
            
        res = []
        for C, D in queries:
            num = 1.0
            ans = dfs(set([]), C, D, num)
            res.append(ans)
            
        return res