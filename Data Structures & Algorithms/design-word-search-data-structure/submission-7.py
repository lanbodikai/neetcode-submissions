class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            curr = node

            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    for c in curr.children.values():
                        if dfs(j + 1, c):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end    

        return dfs(0,self.root)  
