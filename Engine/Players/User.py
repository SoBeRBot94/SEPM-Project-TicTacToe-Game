import ast


class _User:
    """
    Class which is used by the human player. Shouldn't be called directly, instead, call it via the class Player.
    """
    def nextMove(self, board, currentPlayer):
        """

        Runs the method nextMove for the class which was initialized.

        :param board: The 3x3 board from GameEngine. On the form of List[List,List,List]
        :param currentPlayer: The player who is making the next move (X or O)
        :returns: The row and column for the next move. On the form of (rowIdx, colIdx)
        :rtype: tuple
        """
        self._nextMove(board)
        return self.getMove()

    def getMove(self):
        """

        Returns the value stored in self.move which is the next chosen move for the AI.

        :returns: The with the row and column for the next move. On the form of (rowIdx, colIdx)
        :rtype: tuple
        """
        return self.move

    def _nextMove(self, board):
        """
        :param board: The 3x3 board from GameEngine.
        :type board: List[List[int]]
        .. note:: Waits for input from the User regarding the next move. It then checks if the move is
            a valid one. If it is, the move is saved to self, but if the move isn't valid, a ValueError is raised.
        """
        moveCandidate = ast.literal_eval(input())
        possibleMoves = self.getPossibleMoves(board)
        if moveCandidate in possibleMoves:
            self.move = moveCandidate
        else:
            raise ValueError('Not a possible move, pick a new move.')

    def getPossibleMoves(self, board):
        """
        :param board: The 3x3 board from GameEngine.
        :type board: List[List[int]]
        :returns: The possible moves left on the board.
        :rtype: List[tuple]
        """
        possibleMoves = []
        for rowIdx, row in enumerate(board):
            for colIdx, column in enumerate(row):
                if column == None:
                    possibleMoves.append((rowIdx, colIdx))
        return possibleMoves
