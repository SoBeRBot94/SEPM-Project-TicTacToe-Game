from AI import _AI
from User import _User


class Player(object):
    """
    The class which controls if it's a human player or an AI.
    Can take two parameters as input, where the type of the player (AI or user) is mandatory
    A second parameter, difficulty, is not needed when initializing a user type of player
    but it is mandatory when initializing a AI. If trying to initialize an AI without the difficulty
    parameter, a ValueError is raised from the _AI class. If trying to initialize the Player class
    without specifying that the player is a 'ai' or a 'user', a ValueError is raised notifying the client of this.
    The only public facing method which is used by the client is nextMove.
    """
    def __init__(self, typePlayer, difficulty='default'):
        if typePlayer.lower() == 'ai':
            self._Player = _AI(difficulty)

        elif typePlayer.lower() == 'user':
            self._Player = _User()
        else:
            raise ValueError('The stated player is not an AI nor a user. ' \
                             'Please make sure one of those have been stated.')

    def nextMove(self, board, currentPlayer):
        """

        Runs the method nextMove for the class which was initialized.

        :param board: The 3x3 board from GameEngine
        :param currentPlayer: The player who is making the next move (X or O)
        :returns: tuple with the row and column for the next move. On the form of (rowIdx, colIdx)
        """
        return self._Player.nextMove(board, currentPlayer)
