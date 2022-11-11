# LeetCode 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

'''
여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.

- 다음 가격과의 차이가 0보다 크다면 더해주는 방식으로 풀이
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(len(prices)-1):
            res = prices[i+1] - prices[i]
            if res > 0:
                answer += res

        return answer