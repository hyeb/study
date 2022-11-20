# LeetCode 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/description/

'''
(h, k) => (키, 앞에 서있는 사람 수)
- 키를 기준으로 먼저 정렬을 시키고 큰 순으로 하나씩 pop()
- k를 인덱스로해서 넣어주기
'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x : (x[0], -x[1])) # h 오름차순, k 내림차순
        res = []
        while people:
            person = people.pop()
            # insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수
            res.insert(person[1], person) 
        return res