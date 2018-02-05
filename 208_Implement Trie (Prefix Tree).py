class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) > 0:
            if word[0] in self.tree:
                self.tree[word[0]].insert(word[1:None])
            else:
                self.tree[word[0]] = Trie()
                if len(word) > 1:
                    self.tree[word[0]].insert(word[1:None])


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word[0] in self.tree:
            if len(word) == 1:
                return True
            else:
                return self.tree[word[0]].search(word[1:None])
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix[0] in self.tree:
            if len(prefix) == 1:
                return True
            else:
                return self.tree[prefix[0]].startsWith(prefix[1:None])
        else:
            return False



