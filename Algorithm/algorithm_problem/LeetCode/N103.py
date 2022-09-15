# LeetCode 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# 이진트리의 root가 주어졌을때, 지그재그 깊이에 맞는 각 노드의 값을 반환

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q, res = collections.deque([root]), []
        depth = 0
        while q:
            temp =[]
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if depth % 2 == 0:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)    
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(temp)
            depth += 1
        
        return res

# 기존의 102번 문제 푼거랑 비슷하게 가는데 각 층별로 깊이를 카운트해서 짝수, 홀수에 따라 queue에 넣는 왼쪽, 오른쪽 노드의 순서를 바꿔주었다.
# 근데 테스트 케이스 [1,2,3,4,null,null,5]인 경우에서 오답
# Output: [[1],[3,2],[5,4]]
# Expected: [[1],[3,2],[4,5]]

# queue에 넣어주는 부분을 다시 고민해봐야할것같다