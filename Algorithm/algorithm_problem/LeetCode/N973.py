# LeetCode 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

# 평면상에 points 목록이 있을 때, 원점 (0,0)에서 k번 가까운 점 목록을 순서대로 출력 (평면상 두 점의 거리는 유클리드 거리)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 요렇게 간단하게 만들 수 있었닷.. 시간 복잡도는 아래와 엄청 차이나지는 않음
        # points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        # return points[:k]

        lst = []
        for x, y in points:
            # dist = x**2 + y**2
            dist = sqrt(x**2 + y**2)
            lst.append((dist, [x,y]))

        lst.sort()

        res = []
        for i in range(k):
            res.append(points[i][1])
        return res



# 딕셔너리 형태로 저장해서 풀려고했는데 복잡해서 이럴 필요 없겠다는 생각이 들었음
#         dic = {}
#         for x, y in points:
#             dist = sqrt(x**2+y**2)
#             if dist not in dic:
#                 dic[dist] = [x,y]
#             else: dic[dist].append([x,y])
        
#         distance = sorted(dic.keys())
#         print(distance)
#         res = []
#         for i in range(k):
#             res.append(dic[distance[i]])
        
#         return res