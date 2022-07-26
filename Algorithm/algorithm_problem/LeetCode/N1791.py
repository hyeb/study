# 1791. Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = {}
        # 간선 하나씩 빼오기
        for k, v in edges:
            if k in dic: # 만약 첫번째것이 dic 안에 있으면 append
                dic[k].append(v)
            else: # 없음 만들어주고
                dic[k] = [v]
            if v in dic: # 양방향이니까 반대의 경우도 생각해주기
                dic[v].append(k)
            else:
                dic[v] = [k]
        
        ans = 0
        for k in dic.keys(): # keys 하나씩 확인해서
            if len(dic[k]) == len(edges): # edges 개수와 같은 k 찾기
                ans = k
        return ans