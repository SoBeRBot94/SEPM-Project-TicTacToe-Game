from AI import *
from User import User

class Player(object):

    def __init__(self, typePlayer, difficulty='default'):
        if typePlayer.lower() == 'ai':
            self._Player = AI(difficulty)

        elif typePlayer.lower() == 'user':
            self._Player = User()
        else:
            raise ValueError('The stated player is not an AI nor a user. ' \
                             'Please make sure one of those have been stated.')

    def nextMove(self, board, currentPlayer):
        return self._Player.nextMove(board, currentPlayer)
