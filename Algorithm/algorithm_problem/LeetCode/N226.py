# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                oth = node.left
                node.left = node.right
                node.right = oth
                q.append(node.left)
                q.append(node.right)
                
        return root