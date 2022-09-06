# LeetCode 701. Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# 주어진 이진 검색 트리에서 특정 값을 올바른 노드에 삽입 후 root를 반환
# val 값은 이진검색트리에 없다고 가정.

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val > val:
                if root.left: # left에 값이 있다면 다시 탐색
                    self.insertIntoBST(root.left, val)
                else: # 없다면 val 넣어주기
                    root.left = TreeNode(val)
            else:
                if root.right: # 마찬가지로 right
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
        else:
            root = TreeNode(val) # [] 이 주어질 경우
        return root