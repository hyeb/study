# LeetCode 148. Sort List
# https://leetcode.com/problems/sort-list/

# - head에서 값을 하나씩 빼와서 리스트에 넣어줌
# - 리스트 상태로 정렬
# - 리스트를 다시 ListNode로 만들어줌
# List -> ListNode 만들어주는 부분이 헷갈려서 책 참고


class Solution:            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        def get_lst(answer, node):
            if node:
                answer.append(node.val)
                get_lst(answer, node.next)
                
        get_lst(answer, head)
        answer = sorted(answer)
        
        p = head
        for i in range(len(answer)):
            if p:
                p.val = answer[i]
                p = p.next
        return head
        