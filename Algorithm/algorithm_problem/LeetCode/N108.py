# LeetCode 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# 오름차순으로 되어있기 때문에 중앙 값이 root가 되어야함

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2 # root가 될 중앙값 먼저 구하기
        
        tree = TreeNode(nums[mid]) # root
        # for m in range(mid, -1, -1):
        #     tree.left = nums[m]
        # for m in range(mid+1, len(nums)):
        #     tree.right = nums[m]
            
        tree.left = self.sortedArrayToBST(nums[:mid]) # left 노드는 mid 왼쪽 탐색
        tree.right = self.sortedArrayToBST(nums[mid+1:]) # right 노드는 mid 오른쪽 탐색
    
        return tree