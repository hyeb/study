# LeetCode 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# 이진 트리가 주어졌을때, 층별로 순회하며 순서대로 층별 요소의 목록을 반환
# 층별로 순회이기 때문에 bfs
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q, ans = collections.deque([root]), [] # root를 queue로 
        while q:
            temp = [] # 각 층별 노드를 담을 리스트
            for _ in range(len(q)):
                node = q.popleft() 
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(temp)
        return ans

# 이 문제는 코드 하나하나 뜯어보니 이해가는데 지그재그문제는 아직도 헷갈린다..
# 참고
# https://zhenyu0519.github.io/2020/03/18/lc102/