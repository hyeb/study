# LeetCode N46, Permutations
# https://leetcode.com/problems/permutations/

# 푸는 방법: 백트래킹, itertools.permutations
# 데이터 수가 적으면 내장함수 이용이 편하겠지만, 
# 데이터 수가 많다면 메모리 및 시간이 오래걸리기 때문에 이런 문제처럼 가능한 모든 조합을 찾는 문제는 백트래킹을 사용하는것이 좋음


## 백트래킹 사용
sclass Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # visited가 필요 없는듯

        answer = []
        
        def bt(sets):
            if len(sets) == len(nums):
                answer.append(sets.copy()) # 종료조건
                return

            for n in nums:
                if n in sets: # n이 sets안에 있다면 다음 수로 넘어가기
                    continue

                sets.append(n)
                bt(sets)
                sets.pop()
        
        bt([])
        return answer


## itertools.permutations 사용
from itertools import permutations

class Solution:
    def permute(self, nums):
        return list(permutations(nums))