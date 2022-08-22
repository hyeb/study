# LeetCode 104, Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(root)
        if root is None:
            return 0
        
        q = deque([root])
        depth = 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft() # 왼쪽에서 뽑아야하는데 이걸 그냥 pop해버렸,,
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            depth += 1
        
        return depth

# deque로 bfs 방식으로 풀었다 (사실 내가 풀었다기보다는 아이디어를 참고했다)