# LeetCode 134. Gas Station
# https://leetcode.com/problems/gas-station/description/

'''
원형으로 경로가 연결된 주유소 목록이 있다. 각 주유소는 gas[i]만큼의 기름을 갖고 있으며, 다음 주유소로 이동하는데 cost[i]가 필요하다. 
기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점의 인덱스를 출력하라.
출발점이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일하다.

- 주유소 순서대로 시작점으로 기준을 잡고 탐색
- 기름이 부족한 상황이 생긴다면 다음 주유소로 넘어가기 
- 아니라면 해당 번째 주유소를 시작점으로 잡고 여행 가능한지 탐색
- 연료가 부족한 지점이 생긴다면 can = False 전부 가능하면 ith 반환
모든 주유소 탐색이 가능한가 아닌가에 대한 부분을 참고했는데, 결국 O(n2)이라서 시간초과 발생..

=> fue += 부분을 좀더 고민해보기
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        fuel = 0
        for ith in range(len(gas)):
            # can = True
            fuel += gas[ith] - cost[ith]
            # print('ith', ith, 'fuel', fuel)
            if fuel < 0:
                fuel = 0
                continue
            else:
                # return ith
                can = True
                for j in range(ith+1, len(gas)+ith+1):
                    idx = j % len(gas)
                    fuel += gas[idx] - cost[idx]
                    # print('idx', idx, 'fuel', fuel)
                    if fuel < 0:
                        can = False
                        break
                if can:
                    return ith
        return -1