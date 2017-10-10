class GameEngine:
    """
    When initializing GameEngine, a board 3x3 board is filled with the values of None. The first player
    is always player 'X', whilst the second player is always the player 'O'.
    """
    def __init__(self, startingPlayer):
        self.board = [[None for i in range(3)] for i in range(3)]
        self.player = startingPlayer
        

    def getPlayer(self):
        """
        :returns: The player whose turn it is - 'X' or 'O'.
        :rtype: String
        """
        return self.player

    def changePlayer(self):
        """

        Changes the current player that is to play on the board. Saves it to self.

        """
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def getBoard(self):
        """
        :returns: The current board.
        :rtype: List[List[String]]
        """
        return self.board

    def updateBoard(self, player, move):
        """
        :param player: The player that is making a move.
        :param move: The move that the player has chosen to play.
        :type player: String
        :type move: tuple
        :returns: Nothing. The updated board is saved in self.board.
        .. note:: Raises a ValueError if the move is invalid.
        """
        if self.board[move[0]][move[1]] == None:
            self.board[move[0]][move[1]] = player
        else:
            raise ValueError("Invalid move.")

    def isFinished(self, board):
        """
        :param board: The 3x3 board from GameEngine.
        :type board: List[List[String]]
        :returns: A boolean stating if the game is finished or if there are still moves left to be placed.
        :rtype: Boolean
        """
        for i in range(0,3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] !=            None:
                return True

            if board[i][0] == board[i][1] == board[i][2] and board[i][0] !=            None:
                return True

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
            return True
        if board[2][0] == board[1][1] == board[0][2] and board[2][0] != None:
            return True

        return not any(None in row for row in board)

    def resetBoard(self):
        """

        Resets the board for a new game.

        """
        self.board = [[None for i in range(3)] for i in range(3)]
        self.player = 'X'
        self.nextMove = None

    def getResult(self, board):
        """
        :param board: The 3x3 board from GameEngine.
        :type board: List[List[String]]
        :returns: The result from the board with the values being either 'X', 'O', or tie
        :rtype: String
        """
        for i in range(0,3):
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

            if board[i][0] == board[i][1] == board[i][2]:
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[2][0] == board[1][1] == board[0][2]:
            return board[2][0]

        return 'tie'

