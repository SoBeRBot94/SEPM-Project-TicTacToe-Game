import unittest
from GameEngine import GameEngine
from Players.AI import _AI

class firstCase(unittest.TestCase):

    def setUp(self):
        self.GameEngine = GameEngine()
        self.ai = _AI('hard')
        

    def testIsFinished1(self):
        board = [[None,None,None],[None,None,None],[None,None,None]]
        assert self.GameEngine.isFinished(board) == False,\
            "Wrong with empty board."

    def testIsFinished2(self):
        board = [['X','X','X'], [None, None, None],[None, None, None]]
        assert self.GameEngine.isFinished(board) == True, \
            "Wrong with win in a row."

    def testIsFinished3(self):
        board = [['X', None, None], [None,'X',None],[None, None, 'X']]
        assert self.GameEngine.isFinished(board) == True, \
                "Wrong with diagonal win."

    def testIsFinished4(self):
        board = [['X','O','X'], [None, None, None], [None, None, None]]
        assert self.GameEngine.isFinished(board) == False,\
        "Three values in a row, but theyre not from the same player."

    def testChangePlayer(self):
        currentPlayer = 'X' #Game always starts with player X.
        self.GameEngine.changePlayer()
        differentPlayer = self.GameEngine.getPlayer()
        assert differentPlayer == 'O', \
                "Doesn't switch players properly."

    def testUpdateBoard1(self):
        currentPlayer = 'X'
        self.GameEngine.updateBoard(currentPlayer, (0,1))
        board = self.GameEngine.getBoard()
        assert board == [[None, 'X', None], [None, None, None], [None, None, None]], "Wrong when updating board"





if __name__ == '__main__':
    unittest.main()
