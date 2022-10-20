# LeetCode 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

# m x n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라. 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬 되어있음.

# 이진탐색 함수 만들고 모든 행을 이진탐색하면서 target을 찾는 방식으로 풀이

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(lst, target):
            left, right = 0, len(lst)-1
            while left <= right:
                mid = (left+right) // 2
                if lst[mid] == target:
                    return True
                elif lst[mid] < target:
                    left += 1
                else:
                    right -= 1
            return False
        
        for lst in matrix:
            if binary(lst, target):
                return True
        return False
            