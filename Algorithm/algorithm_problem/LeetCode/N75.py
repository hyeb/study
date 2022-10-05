# LeetCode 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

# 빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리 정렬을 수행
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]


# 버블 정렬 사용
# 피드백
# 해당 문제의 조건은 n<=300이라 크게 문제되지는 않지만 n이 커지면 
# 최악의 경우 시간복잡도가 O(n**2)라서 더 좋은 방법을 찾아보면 좋을 것 같음