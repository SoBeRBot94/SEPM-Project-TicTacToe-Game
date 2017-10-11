import copy
from collections import Counter
import random
from abc import ABC, abstractmethod

class _AI(object):
    """Class which is used to initialize an AI type of player. Shouldn't be called directly, instead,
    call it via the class Player. The class _AI, which receives the difficulty parameter from the initialization
    of the Player class, uses it to be able to initialize the correct difficulty of the AI.
    If the difficulty parameter isn't one of the following: hard, medium or easy, a ValueError is raised
    notifying the client of this."""

    def __init__(self, difficulty):
        # self.move = None
        if (difficulty.lower() == "hard"):
            self._AI = _AIHard()
        elif (difficulty.lower() == "medium"):
            self._AI = _AIMedium()
        elif (difficulty.lower() == "easy"):
            self._AI = _AIEasy()
        else:
            raise ValueError(
                'The difficulty of the AI is not one of the following: \
                easy, medium or hard. The AI could not be initialized')

    def nextMove(self, board, currentPlayer):
        """

        Runs the method nextMove for the class which was initialized.

        :param board: The 3x3 board from GameEngine. On the form of List[List,List,List]
        :param currentPlayer: The player who is making the next move (X or O)
        :returns: The row and column for the next move. On the form of (rowIdx, colIdx)
        :rtype: tuple
        """
        self._AI.nextMove(board, currentPlayer)
        return self._AI.getMove()


"""
Start of module methods
"""
def emptyBoard():
    """
        Creates an empty board.
        :returns: an empty board
        :rtype: [[String]]
    """
    return [[None, None, None], [None, None, None], [None, None, None]]

def isTerminalState(board):
    """
    :param board: The 3x3 board from GameEngine.
    :type board: List[List[String]]
    :returns: The state of the current board.
    """
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != None:
                return board[0][i]
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != None:
                return board[i][0]

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != None:
            return board[2][0]

    if getPossibleMoves(board) == []:
        return 'tie'

    return None

def getPossibleMoves(board):
    """
    :param board: The 3x3 board from GameEngine.
    :type board: List[List[String]]
    :returns: The possible moves left on the board.
    :rtype: List[tuple]
    """
    possibleMoves = []
    for rowIdx, row in enumerate(board):
        for colIdx, column in enumerate(row):
            if column == None:
                possibleMoves.append((rowIdx, colIdx))
    return possibleMoves

def nextState(board, move, player):
    """
    Creates a copy of the given board with the given move of the given player added.

    :param board: The 3x3 board from GameEngine.
    :type board: List[List[String]]
    :param move: The move to be made.
    :type move: (row, column)
    :param player: The player making the move.
    :type player: String
    :returns: A copy of the given board with the given move of the given player added.
    :rtype: List[List[String]]
    """
    if (board[move[0]][move[1]] == None):
        # makes a copy of the board
        boardCopy = copy.deepcopy(board)
        # updates the copy with the given move
        boardCopy[move[0]][move[1]] = player
        return boardCopy

        # illegal move should, throw error or something.
    # returns a copy of the board
    return copy.deepcopy(board)
"""
End of module methods
"""

class _AIAbstract(ABC):
    """
    The abstract class that provides the nextMove and getMove methods, as well as forcing the implementation
    of the _nextMove method.
    """
    def nextMove(self, board, currentPlayer):
        """

        Finds the next move for the AI.

        :param board: The 3x3 board from GameEngine.
        :param currentPlayer: The player who is making the next move ('X' or 'O')
        :type board: List[List[String]]
        :type currentPlayer: String
        """
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'
        self._nextMove(board, currentPlayer)

    @abstractmethod
    def _nextMove(self, board, currentPlayer):
        pass

    def getMove(self):
        """

        Returns the value stored in self.move which is the next chosen move for the AI.

        :returns: The with the row and column for the next move. On the form of (rowIdx, colIdx)
        :rtype: tuple
        """
        return self.move

class _AIHard(_AIAbstract):
    """
    Class which is the hardest AI. Shouldn't be called directly, instead, call it via the class _AI which is
    called via the class Player. It has no initialization parameters as it is given that it should go via the _AI class.
    """

    def _nextMove(self, board, currentPlayer):
        """

        Minimax algorithm to find the optimal move for the AI.

        :param board: The 3x3 board from GameEngine.
        :param currentPlayer: The player who is making the next move ('X' or 'O')
        :type board: List[List[String]]
        :type currentPlayer: String
        :returns: The optimal score retrieved through the use of the minimax algorithm
        :rtype: int
        .. note:: The next move is stated here as well, but it is saved to self with the line self.move = move. This is
            because the algorithm works recursively and the value the algorithm follows is the score.
        """
        if (isTerminalState(board)):
            return self.score(board)
        if (board == emptyBoard()):
            self.move = (0, 0)
            return
        possibleMoves = getPossibleMoves(board)
        scores = []
        moves = []
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'
        for move in possibleMoves:
            possibleNewBoard = nextState(board, move, currentPlayer)
            score = self._nextMove(possibleNewBoard, currentPlayer)
            moves.append(move)
            scores.append(score)

        if currentPlayer == 'X':
            maxScoreIdx = scores.index(max(scores))
            self.move = moves[maxScoreIdx]
            return max(scores)
        else:
            minScoreIdx = scores.index(min(scores))
            self.move = moves[minScoreIdx]
            return min(scores)

    def score(self, board):
        """

        The score to be retrieved for the minimax algorithm.

        :param board: The 3x3 board from GameEngine.
        :type board: List[List[String]]
        :returns: The score used for the minimax algorithm
        :rtype: int
        """
        winner = isTerminalState(board)
        if winner == 'X':
            return 10
        elif winner == 'O':
            return -10
        elif winner == 'tie':
            return 0

class _AIMedium(_AIAbstract):
    """
    Class which is the medium AI. Shouldn't be called directly, instead, call it via the class _AI which is
    called via the class Player. It has no initialization parameters as it is given that it should go via the _AI class.
    """

    def _nextMove(self, board, currentPlayer):
        """
        :param board: The 3x3 board from GameEngine.
        :param currentPlayer: The player who is making the next move ('X' or 'O')
        :type board: List[List[String]]
        :returns: Return is empty as it is used instead of a break.
        :rtype: NoneType
        .. note:: The algorithm for the medium level AI is the following:
            If opponent has two in a row -> AI will block. If AI has two in a row -> AI will place the winning move.
            Otherwise, the AI will just choose a placement at random. The move that is going to be placed is saved
            to self via self.move.
        """
        for rowIdx, row in enumerate(board):
            if 2 in Counter(row).values() and Counter(row)[None] == 1:
                colIdx = row.index(None)
                self.move = (rowIdx, colIdx)
                return

        for colIdx, col in enumerate(list(zip(*board))):
            if 2 in Counter(col).values() and Counter(col)[None] == 1:
                rowIdx = col.index(None)
                self.move = (rowIdx, colIdx)
                return

        diagonal1 = [board[0][0], board[1][1], board[2][2]]
        if 2 in Counter(diagonal1).values() and Counter(diagonal1)[None] == 1:
            idx = diagonal1.index(None)
            self.move = (idx, idx)
            return

        diagonal2 = [board[2][0], board[1][1], board[0][2]]
        if 2 in Counter(diagonal2).values() and Counter(diagonal2)[None] == 1:
            idx = diagonal2.index(None)
            if idx == 0:
                self.move = (2, idx)
            elif idx == 1:
                self.move = (idx, idx)
            elif idx == 2:
                self.move = (0, idx)
            return

        possibleMoves = getPossibleMoves(board)
        self.move = random.SystemRandom().choice(possibleMoves)

class _AIEasy(_AIAbstract):
    """
    Class which is the easiest AI. Shouldn't be called directly, instead, call it via the class _AI which is
    called via the class Player. It has no initialization parameters as it is given that it should go via the _AI class.
    """

    def _nextMove(self, board, currentPlayer):
        """
        :param board: The 3x3 board from GameEngine.
        :param currentPlayer: The player who is making the next move ('X' or 'O')
        :type board: List[List[String]]
        :type currentPlayer: String
        .. note:: The easy algorithm retrieves all the possible moves on the board and then chooses the next
            placement at random. The move is then saved to self.
        """
        possibleMoves = getPossibleMoves(board)
        self.move = random.SystemRandom().choice(possibleMoves)
