# LeetCode 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

# 1. 각 노드의 시간이 담긴 graph 생성
# 2. 다익스트라 알고리즘을 사용

# 참고: https://velog.io/@pyh8618/LeetCode-743.-Network-Delay-Time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        # 간선 정보 
        for a, b, c in times:
            graph[a].append((b,c))
        
        print(graph)
        
        q = [(0, k)] # time, node
        dist = collections.defaultdict(int)
        
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
        print(dist)
        if len(dist) == n:
            return max(dist.values())
        return -1
