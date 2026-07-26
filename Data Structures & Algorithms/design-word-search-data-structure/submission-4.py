class WordDictionary:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.data:
                curr.data[w] = WordDictionary()
            curr = curr.data[w]
        curr.is_word = True
    
    def search(self, word: str) -> bool:
        curr = self
        for i, w in enumerate(word):
            if w == ".":
                for pf in curr.data.values():
                    if pf.search(word[i+1:]):
                        return True
                return False
            elif w not in curr.data:
                return False
            curr = curr.data[w]
        return curr.is_word

        
