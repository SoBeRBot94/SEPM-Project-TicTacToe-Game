import unittest
from AI import AI
from GameEngine import GameEngine
class caseAIHard(unittest.TestCase):

    def setUp(self):
        self.ai = AI("hard")
        self.ge = GameEngine()
    def testWinningMove(self):
        currentPlayer = 'X'
        #board = self.ge.getBoard()
        #self.ge.updateBoard('X', (0,0))
        #self.ge.updateBoard('O', (1,0))
        #self.ge.updateBoard('X', (0,1))
        #self.ge.updateBoard('O', (1,1))
        #print(board)
        board = [['X', 'X', None],[None, None, None],[None, None, None]]
        print(board)
        nextMove = self.ai.nextMove(board, currentPlayer)
        #nextMove = self.ai.getMove()
        print(nextMove)

if __name__ == '__main__':
    unittest.main()
