# LeetCode 783. Minimum Distance Between BST Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# 두 노드간 값의 차이가 가장 적은 값을 반환
# 재귀적으로 탐색할건데 전 노드의 값을 저장해두고 그 다음노드와 비교해서 최소값만 업데이트

class Solution:
    prev, ans = -1e5, 1e5   # 0 <= Node.val <= 10^5 조건
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left: # 왼쪽부터
            self.minDiffInBST(root.left)
        
        self.ans = min(self.ans, abs(self.prev - root.val))
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)
        
        return self.ans