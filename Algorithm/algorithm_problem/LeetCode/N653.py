# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        roots = []
        def root_num(node):
            if node:
                roots.append(node.val)
                root_num(node.right)
                root_num(node.left)
        
        root_num(root)
        
        for i in roots:
            for j in roots:
                if i != j and i + j == k:
                    return True
        return False