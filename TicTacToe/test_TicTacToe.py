import unittest
from GameBoard import GameBoard
from Players import Players
from InvalidCellNumberException import InvalidCellNumberException
from CellOccupiedException import CellOccupiedException

class TicTacToeTest(unittest.TestCase):

    def test_make_move(self):
        board = GameBoard()
        players = Players("X", "O")
        players.make_move(board, 0, 0)
        self.assertEqual(board.board[0][0], "X")
        with self.assertRaises(InvalidCellNumberException):
            players.make_move(board, -1, 0)

        # Try to make a move on an occupied cell
        with self.assertRaises(CellOccupiedException):
            players.make_move(board, 0, 0)

    def test_is_full(self):
        board = GameBoard()
        players = Players("X", "O")

        # Make the board full
        for row in range(3):
            for col in range(3):
                players.make_move(board, row, col)

        self.assertTrue(board.is_full())

        # Make a move on a non-full board
        board = GameBoard()
        players.make_move(board, 0, 0)
        self.assertFalse(board.is_full())

    def test_get_winner(self):
        board = GameBoard()
        players = Players("X", "O")

        # Test a win by X in a row
        players.make_move(board, 0, 0)
        players.make_move(board, 0, 1)
        players.make_move(board, 0, 2)
        self.assertEqual(board.get_winner(), "X")

        # Test a win by O in a column
        board = GameBoard()
        players.make_move(board, 0, 0)
        players.make_move(board, 1, 0)
        players.make_move(board, 2, 0)
        self.assertEqual(board.get_winner(), "O")

        # Test a win by X in a diagonal
        board = GameBoard()
        players.make_move(board, 0, 0)
        players.make_move(board, 1, 1)
        players.make_move(board, 2, 2)
        self.assertEqual(board.get_winner(), "X")

        # Test a tie
        board = GameBoard()
        for row in range(3):
            for col in range(3):
                players.make_move(board, row, col)
        self.assertEqual(board.get_winner(), None)
