import unittest
from tkinter import *
from tkinter import messagebox
from tictac import *

class testClassSortedFile(unittest.TestCase):
    mainWin = Tk()
    ttt = TTT(mainWin)

    def test_NoResult(self):
        mainWin = Tk()
        ttt = TTT(mainWin)
        ##ttt.clicked(ttt.B22)
        result = ttt.playerWon([ " ", " ", " ", " ", " ", " ", " ", " ", " "],"X")
        self.assertFalse(result)

    def test_CorrectResult(self):
        mainWin = Tk()
        ttt = TTT(mainWin)
        ##ttt.clicked(ttt.B22)
        result = ttt.playerWon([ "X", "X", "X", " ", " ", " ", " ", " ", " "],"X")
        self.assertTrue(result)

    def test_emptyIndex(self):
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        mainWin = Tk()
        ttt = TTT(mainWin)
        result = len(ttt.emptyIndexes(board))
        self.assertEqual(result, 9)

    def test_createBoard(self):
        mainWin = Tk()
        ttt = TTT(mainWin)
        ttt.redrawBoard()

    def test_move(self):
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        mainWin = Tk()
        ttt = TTT(mainWin)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testClassSortedFile)
    unittest.TextTestRunner(verbosity=0).run(suite)
