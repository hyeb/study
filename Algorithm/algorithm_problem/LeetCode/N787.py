# LeetCode 787, Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/


import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)     
        for start, end, price in flights:
            graph[start].append((end, price))
        # print(graph)
        
        # (price, node, stops)
        q = [(0, src, k)]
        visited = dict()
        
        while q:
            price, node, stops = heapq.heappop(q)
            if node == dst:
                return price
            if node not in visited and stops > k:
                visited[node] = stops
                for n, p in graph[node]:
                    if stops <= k:
                        heapq.heappush(q, (price+p, n, stops-1)) 
        return -1      


# 다익스트라 알고리즘
# 1. 출발 노드를 설정
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소비용을 갱신
# 5. 위 과정에서 3~4를 반복


# 이전 코드
# from collections import deque, defaultdict
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = [[] for _ in range(n+1)]       
#         for start, end, price in flights:
#             graph[start].append([end, price])
#         print(graph)
        
#         def bfs(start):
#             stops = 0
#             price = 0
#             q = [src]
#             while q:
#                 city = q.pop()
#                 if city == dst:
#                     return price
#                 if stops != k:
#                     stops += 1
#                     for node in graph[city]:
#                         price += node[1]
#                         q.append(node[0])
#                 else:
#                     return -1
                    
#         bfs(src)
