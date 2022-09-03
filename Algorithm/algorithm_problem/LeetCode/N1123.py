# LeetCode 1123. Lowest common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# LCA는 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제
# -> 그래서 가장 깊은 노드를 먼저 탐색하고 그 노드에서 LCA를 찾으면 된다고 한거구나 

# LCA의 알고리즘 동작 순서는 먼저 두 노드의 깊이를 맞춰주는거라고 하지만 여기선 두 노드가 주어지지 않음.

# 우리는 일단 깊이만을 먼저 고려해서 탐색할 것.
# 가장 깊은 노드를 탐색한다는 것은 그런 의미. 깊이가 2인 노드가 있는데 1인 노드를 고려할 필요가 없음.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getDepth(node, level): # bottom-up 방식
            # 결국 이 함수는 현재 노드의 깊이를 찾아내는 함수
            nonlocal ans, depth_level
            depth_level = max(depth_level, level)
            
            if not node: # 더이상 탐색할 left,right가 없으면 그 노드의 레벨을 반환
                return level

            left_level = getDepth(node.left, level+1)
            right_level = getDepth(node.right, level+1)

            if left_level == right_level == depth_level: # 왼쪽 깊이, 오른쪽 깊이, 최대 깊이가 같다면 => 최대 깊이 노드까지 찾아갔다면.
                ans = node # 해당하는 현재 노드가 답이 됨

            return max(left_level, right_level)

        depth_level = 0
        ans = None
        getDepth(root, 0)

        return ans 