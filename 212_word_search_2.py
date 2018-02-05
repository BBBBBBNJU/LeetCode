class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        prefTree = {}
        for word in words:
            c = prefTree
            for w in word:
                if w not in c:
                    c[w] = {}
                c = c[w]
            c['#'] = '#'

        dim1 = len(board)
        dim2 = len(board[0])

        self.results = set()
        self.visit = [[False for i in range(dim2)] for j in range(dim1)]

        for i in range(dim1):
            for j in range(dim2):
                self.dfs(board, i, j, prefTree, '')

        return self.results

    def dfs(self, board, i, j, tree, pref):
        if '#' in tree:
            self.results.add(pref)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.visit[i][j] and board[i][j] in tree:
            self.visit[i][j] = True
            self.dfs(board, i+1, j, tree[board[i][j]], pref + board[i][j])
            self.dfs(board, i, j+1, tree[board[i][j]], pref + board[i][j])
            self.dfs(board, i-1, j, tree[board[i][j]], pref + board[i][j])
            self.dfs(board, i, j-1, tree[board[i][j]], pref + board[i][j])
            self.visit[i][j] = False
