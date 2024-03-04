class GameBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, player, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            raise InvalidCellNumberException("Invalid cell number")
        if self.board[row][col] != ' ':
            raise CellOccupiedException("Cell already occupied")
        self.board[row][col] = player

