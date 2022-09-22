# LeetCode 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

# 트라이를 구현하면 되는 문제
# Trie를 만들어주고 마지막 노드.data가 True일 경우 단어가 존재한다는 의미이므로 True 반환
# 주어진 단어 = apple, app을 search 했을 때 apple 이라는 단어가 있는거지 app 는 없기 때문에 false 처리를 해줘야 함

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, word: str) -> None:
        curr_node = self.head
        
        for w in word:
            if w not in curr_node.children:
                curr_node.children[w] = Node(w)
                
            curr_node = curr_node.children[w]
        curr_node.data = word
        
    def search(self, word: str) -> bool:
        curr_node = self.head
        
        for w in word:
            if w in curr_node.children:
                curr_node = curr_node.children[w]
            else:
                return False
        
        if curr_node.data is not None:
            return True

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.head
        for p in prefix:
            if p not in curr_node.children:
                return False
            curr_node = curr_node.children[p]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)