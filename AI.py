import copy

class AI(object):
    def __init__(self, difficulty):
        #self.nextMove = None
        if (difficulty.lower() == "hard"):
            self._AI = AIHard()

    def nextMove(self,board, currentPlayer):
        self._AI.nextMove(board, currentPlayer)
        return self._AI.getMove()

class AIHard:

    def nextMove(self, board, currentPlayer):
        self._optimalNextMove(board, currentPlayer)
        #return self.nextMove

    def getMove(self):
        return self.move

    def _optimalNextMove(self, board, currentPlayer):
        if (self.isTerminalState(board)):
            return self.score(board)
        possibleMoves = self.getPossibleMoves(board)
        scores = []
        moves = []
        #currentPlayer = 'O'
        if currentPlayer == 'X':
            currentPlayer = 'O'
        else:
            currentPlayer = 'X'
        for move in possibleMoves:
            possibleNewBoard = self.nextState(board, move, currentPlayer)
            score = self._optimalNextMove(possibleNewBoard, currentPlayer)
            moves.append(move)
            scores.append(score)

        if currentPlayer == 'X':
            maxScoreIdx = scores.index(max(scores))
            self.move = moves[maxScoreIdx]
            return max(scores)
        else:
            minScoreIdx = scores.index(min(scores))
            self.move = moves[minScoreIdx]
            #print(moves[minScoreIdx])
            return min(scores)
            # self.nextMove = moves[minScoreIdx]
            # return min(scores)

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

    def nextState(self, board, move, player):
        if (board[move[0]][move[1]] == None):
            # makes a copy of the board
            boardCopy = copy.deepcopy(board)
            # updates the copy with the given move
            boardCopy[move[0]][move[1]] = player
            return boardCopy

        # illagal move should, throw error or something.
        # returns a copy of the board
        #Right now, illegal moves just return the same board
        #Without throwing an error, this needs to be fixed.
        return copy.deepcopy(boar)
