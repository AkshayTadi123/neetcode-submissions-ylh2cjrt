class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True


    def search(self, word: str) -> bool:
        return self.search2(word, self.root)
    
    def search2(self, word: str, node: TrieNode) -> bool:
        curr = node
        for i in range(len(word)):
            if word[i] == ".":
                x = False
                for child in curr.children:
                    x = x or self.search2(word[i+1:], curr.children[child])
                    if x:
                        return True
                return x
            else:
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
        return curr.end
