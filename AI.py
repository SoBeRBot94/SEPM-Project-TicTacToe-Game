import copy
from collections import Counter
import random

class AI(object):
    def __init__(self, difficulty):
        #self.nextMove = None
        if (difficulty.lower() == "hard"):
            self._AI = AIHard()
        elif (difficulty.lower() == "medium"):
            self._AI = AIMedium()
        elif (difficulty.lower() == "easy"):
            self._AI = AIEasy()
        else:
            raise ValueError(
                'The difficulty of the AI is not one of the following: \
                easy, medium or hard. The AI could not be initialized')

    def nextMove(self,board, currentPlayer):
        self._AI.nextMove(board, currentPlayer)
        return self._AI.getMove()

class AIHard:

    def nextMove(self, board, currentPlayer):
        self._optimalNextMove(board, currentPlayer)
        #return self.nextMove

    def getMove(self):
        #print(self.move)
        return self.move

    def _optimalNextMove(self, board, currentPlayer):
        if (self.isTerminalState(board)):
            return self.score(board)
        possibleMoves = self.getPossibleMoves(board)
        score = -1
        for move in possibleMoves:
            board[move[0]][move[1]] = currentPlayer
            if currentPlayer == 'X':
                currentPlayer = 'O'
            else:
                currentPlayer = 'X'
            newScore = -self._optimalNextMove(board, currentPlayer)
            if newScore > score:
                score = newScore
                self.move = move
            board[move[0]][move[1]] = None
            return score

    def score(self, board):
        winner = self.isTerminalState(board)
        if winner == 'X':
            return 10
        elif winner == 'O':
            return -10
        elif winner == 'tie':
            return 0

    def isTerminalState(self, board):
        # check win on straigh lines
        for i in range(0, 3):
            # column
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
            # row
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]

        # check win on diagonals
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[2][0] == board[1][1] == board[0][2]:
            return board[2][0]

        # Check if the game has ended in a tie.
        if self.getPossibleMoves(board) == []:
            return 'tie'

        return None

    def getPossibleMoves(self, board):
        possibleMoves = []
        for rowIdx, row in enumerate(board):
            for colIdx, column in enumerate(row):
                if column == None:
                    possibleMoves.append((rowIdx, colIdx))
        return possibleMoves

class AIMedium:

    def nextMove(self, board, currentPlayer):
        self._nextMove(board, currentPlayer)

    def getMove(self):
        return self.move

    def _nextMove(self, board, currentPlayer):
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

        possibleMoves = self.getPossibleMoves(board)
        self.move = random.choice(possibleMoves)


    def getPossibleMoves(self, board):
        possibleMoves = []
        for rowIdx, row in enumerate(board):
            for colIdx, column in enumerate(row):
                if column == None:
                    possibleMoves.append((rowIdx, colIdx))
        return possibleMoves

class AIEasy:

    def nextMove(self, board, currentPlayer):
        self._nextMove(board, currentPlayer)

    def getMove(self):
        return self.move

    def _nextMove(self, board, currentPlayer):
        possibleMoves = self.getPossibleMoves(board)
        self.move = random.choice(possibleMoves)

    def getPossibleMoves(self, board):
        possibleMoves = []
        for rowIdx, row in enumerate(board):
            for colIdx, column in enumerate(row):
                if column == None:
                    possibleMoves.append((rowIdx, colIdx))
        return possibleMoves


