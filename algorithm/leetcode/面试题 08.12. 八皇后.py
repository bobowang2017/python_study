class Solution(object):

    def __init__(self):
        self.board = None
        self.length = -1
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.length = n
        self.back_track(0)
        return self.result

    def back_track(self, row):
        if row == self.length:
            self.result.append([''.join(self.board[x]) for x in range(self.length)])
            return
        for c in range(self.length):
            if not self.is_valid(row, c):
                continue
            self.board[row][c] = 'Q'
            self.back_track(row + 1)
            self.board[row][c] = '.'

    def is_valid(self, row, col):
        # 检查列是否有皇后互相冲突
        for i in range(self.length):
            if self.board[i][col] == 'Q':
                return False

        # 检查右上方是否有皇后互相冲突
        _i = row - 1
        _j = col + 1
        while _i >= 0 and _j < self.length:
            if self.board[_i][_j] == 'Q':
                return False
            _i -= 1
            _j += 1
        # 检查左上方是否有皇后互相冲突
        _i = row - 1
        _j = col - 1
        while _i >= 0 and 0 <= _j:
            if self.board[_i][_j] == 'Q':
                return False
            _i -= 1
            _j -= 1
        return True


s = Solution()
s.solveNQueens(8)
