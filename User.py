import ast
class User:

    def nextMove(self, board, currentPlayer):
        self._nextMove(board)
        return self.getMove()

    def getMove(self):
        return self.move

    def _nextMove(self, board):
        moveCandidate = ast.literal_eval(input())
        possibleMoves = self.getPossibleMoves(board)
        if moveCandidate in possibleMoves:
            self.move = moveCandidate
        else:
            raise ValueError('Not a possible move, pick a new move.')

    def getPossibleMoves(self, board):
        possibleMoves = []
        for rowIdx, row in enumerate(board):
            for colIdx, column in enumerate(row):
                if column == None:
                    possibleMoves.append((rowIdx, colIdx))
        return possibleMoves
