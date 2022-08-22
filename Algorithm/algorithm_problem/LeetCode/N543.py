# LeetCode, Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# easy라고 쉽게보다간 큰코다침~ 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# tree를 돌면서 bfs 한 스텝당 노드를 리스트에 저장하고
# 리스트의 개수를 max로 갱신
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        self.getDepth(res, root)
        return res
    
    def getDepth(self, res: int, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_len = 1 + self.getDepth(res, node.left)
        right_len = 1 + self.getDepth(res, node.right)

        res = max(res, left_len + right_len)

        return res 
    
# tree 탐색하면서 depth를 측정하고 backtracking을 통해 두 자식 노드 사이의 길이를 측정한다. 
# 전체 노드를 모두 탐색한 후 나오는 길이의 최대값이 binary tree의 diameter다.

    
        
#         q = deque([root])
#         left_path = []
#         right_path = []
        
#         while q:
#             node = q.pop()
#             print(node)
#             # left_path.append(node)
#             # right_path.append(node)
            
#             if node.left:
#                 q.append(node.left)
#                 left_path.append(node.left)
#             if node.right:
#                 q.append(node.right)
#                 right_path.append(node.right)

#         ans = max(len(left_path), len(right_path))
#         return ans + 1