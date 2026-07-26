class PrefixTree:
    def __init__(self):
        self.data = {}
        self.is_word = False
        
    def insert(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.data:
                curr.data[w] = PrefixTree()
            curr = curr.data[w]
        curr.is_word = True
            
            
    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            if w not in curr.data:
                return False
            curr = curr.data[w]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for w in prefix:
            if w not in curr.data:
                return False
            curr = curr.data[w]
        return True
        
        