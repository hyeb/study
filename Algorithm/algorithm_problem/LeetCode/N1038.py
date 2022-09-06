# LeetCode 1038. Binary Search Tree to Greater Sum Tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.
# 오른쪽은 항상 큰 수이기 때문에 이걸 기준으로 합을 구하기

class Solution:
    total = 0 
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right) # right 먼저
            # print(right)
            self.total += root.val
            root.val = self.total # 현재노드에 업데이트
            self.bstToGst(root.left) # 후에 left
            
        return root
        