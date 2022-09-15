# LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Binary Tree의 preorder와 inorder가 주어졌을 때 Binary Tree를 만들어 반환
# 전위 순회, 중위 순회로 탐색

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할의 인덱스
            idx = inorder.index(preorder.pop(0))

            # 전위 순회의 첫 번째 노드를 트리의 분할 기점 노드로 잡아 left, right구성
            root = TreeNode(inorder[idx])

            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
        
            return root

# 처음에는 inorder에서 root.left를 만들어주는 함수를 따로 구현해야한다고 생각했는데 그럴필요가 없었다.

# 참고
# https://luckydavekim.github.io/algorithm/leetcode/construct-binary-tree-from-preorder-and-inorder-traversal
# https://zhenyu0519.github.io/2020/03/11/lc105/