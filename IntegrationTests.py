import unittest
from GameEngine.Player import Player
from GamePlatform.Platform import Platform

class integrationTest(unittest.TestCase):
	def setUp(self):
            player1 = Player('test1', 'ai', 'hard')
            player2 = Player('test2', 'ai', 'hard')
            self.Platform = Platform(player1, player2)

	def testIntegration1(self):
                self.Platform.gameState.printBoard()
                self.Platform.gameState.convertBoard()
                self.Platform.gameState.printBoard()
                assert self.Platform.gameState == [[None,None,None],[None,None,None],[None,None,None]] ,\
                        "Conversion of empty board usuccessfull"

                self.Platform.gameState.reConvertBoard()
                assert self.Platform.gameState == [0,0,0,0,0,0,0,0,0] ,\
                        "Reconversion of empty board usuccessfull"

                self.Platform.gameState.AImove(player1, 1)
                assert self.Platform.gameState == [1,0,0,0,0,0,0,0,0] ,\
                        "AI move usuccessfull"

if __name__ == '__main__':
    unittest.main()
