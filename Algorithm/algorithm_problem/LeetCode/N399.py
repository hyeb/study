# LeetCode 399, Evaluate division
# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        dic = defaultdict(list)
        for i in range(len(values)):
            A, B = equations[i]
            dic[A].append((values[i], B))
            dic[B].append((1/values[i], A))
        print(dic)
       
        
        def sol(visited, A, B, num):
            if A == B:
                return num
            
            for new_v, node in dic[A]:
                if not visited[node]:
                    visited[node] = True
                    num *= new_v
                    ans = sol(visited, node, B, num)
                    if ans != -1:
                        visited[node] = False
                        return ans
                    num /= new_v ## else 문 제거하고 이부분 추가해주니까 통과했다!!! (조언주신 분께 매우 큰절)
            return -1            ## visited 방문을 True, False 처럼 처리해주듯이 num도 해당이 안될때 처리를해줘야하는거였다.
            
        res = []
        
        for C, D in queries:
            visited = {k: False for k in dic.keys()}
            num = 1.0
            if C not in dic or D not in dic:
                res.append(-1.0)
                continue
            else:           
                visited[C] = True
                ans = sol(visited, C, D, num)
                visited[C] = False
                res.append(ans)
            
        return res