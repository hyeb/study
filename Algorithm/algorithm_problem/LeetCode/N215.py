# LeetCode 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = sorted(nums, reverse = True)

        return lst[k-1]
    
    # 시간복잡도에서 걸릴거라고 생각하고 그냥 제출해봤는데 통과해서 당황함
    # 근데 오래걸리긴하기때문에 다른 방법으로 풀어봐야겠다
    # heap으로 풀어보라고 조언주셔서 시도해보기