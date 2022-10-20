# LeetCode 2354. Number of Excellent Pairs
# https://leetcode.com/problems/number-of-excellent-pairs/

# 다음 조건이 충족되는 한 쌍의 숫자(num1, num2) 반환
# - 숫자 num1과 num2는 모두 배열 nums에 존재
# - num1 OR num2 및 num1 AND num2에서 설정된 비트 수의 합은 k보다 크거나 같음
# 이게 왜 바이너리서치!!!!?!?!?!

# i를 기준으로 오른쪽에 있는 숫자들을 가져와서 조합을 만들어주는 방식으로 생각했으나 역시 시간초과 남..
# 아직 더 풀어봐야함

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:        
        nums = list(set(nums))
        nums.sort()
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                A, B = bin(nums[i]).count('1'), bin(nums[j]).count('1')
                if A + B >= k:
                    if i == j:
                        res += 1
                    else:
                        res += 2
        return res       
                        