# LeetCode 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

# 한쪽 트리에 더해주는 방식으로 해결
# 예전에 풀었던 트리의 왼쪽, 오른쪽 위치 바꾸는 문제와 비슷한것 같다.

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1