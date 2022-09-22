# LeetCode 1233. Remove Sub-Floders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

# folder 리스트가 주어졌을때, 그 폴더안에 모든 서브 폴더를 제거한 뒤의 폴드들을 return
# 만약 folder[i]가 다른 folder[j] 안에 위치해 있으면 이걸 서브 폴더라고 함

# 일단 주어지는 단어를 split했을 때의 폴더가 1개면 그걸 폴더 리스트에 넣어주고
# 아니라면 폴더 리스트에서 첫번째 폴더가 있는지 확인하고 없으면 전체를 폴더 리스트에 넣어주기
# 있으면 넘어가기
# !!! trie 사용해서 풀어보기 !!!
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        fol = []
        for f in folder:
            flag = False # True일 경우 서브 폴더
            name = f.split('/') # 폴더 명을 /를 기준으로 split
            # print(name)
            if len(name) == 2: # 경로에 폴더가 하나만 있을 경우 (''이 포함되기 때문에 -> '','a')
                fol.append('/' + (name[1])) # 그럼 해당 폴더는 서브 폴더가 아닐테니 폴더 리스트에 넣기
                
            check = ''
            for i in range(1, len(name)): # 경로에 폴더가 여러개일경우
                check += '/' + name[i] # check 문자열에 하나씩 더해주면서 폴더 파일에 있는지 탐색
                if check in fol: # 있다면
                    flag = True # 해당 폴더는 서브 폴더

            if not flag: # 서브 폴더가 아닐 경우
                fol.append(f) # 폴더 리스트에 넣어주기
        # print(f'fol : {fol}')
        # print(f'sub : {sub}')
        
        return fol

# 통과하긴했는데 시간 효율이 많이 안좋았다.
# 그래서 스터디에서 trie를 사용해보라는 조언을 받고 시도했는데 헷갈려서 구현은 아직 못함,,



        # trie = {}
        # for f in folder:
        #     name = f.split('/')
        #     print(f'name: {name}')
        #     curr = trie
        #     for n in name[1:]:
        #         if n not in curr:
        #             curr[n] = {}
        #         curr = curr[n]
        #     curr['*'] = f
        #     print(curr)
        # print(f'trie : {trie}')
        
        # return fol