import unittest
from GameEngine import GameEngine

class firstCase(unittest.TestCase):

    def setUp(self):
        self.GameEngine = GameEngine()

    def testInvalidMove(self):
        self.GameEngine.makeMove(0,0,1)
        board = self.GameEngine.board
        self.GameEngine.makeMove(0,0,2)
        board2 = self.GameEngine.board
        assert board == board2, "Overrides earlier made move. "
        #self.assertRaises(TypeError, GameEngine.makeMove(0,0,1))

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

    #def testUpdateBoard(self):




if __name__ == '__main__':
    unittest.main()
