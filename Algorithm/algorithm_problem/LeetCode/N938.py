# LeetCode 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# 이진트리의 루트노드가 주어지면, L 과 R 값 사이의 값을 가진 모든 노드의 총합을 반환
# 재귀적으로 탐색하면서 범위 안에 들면 + 해주기


class Solution:
    total = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        if low <= root.val <= high:
            self.total += root.val

        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)
        
        return self.total
            