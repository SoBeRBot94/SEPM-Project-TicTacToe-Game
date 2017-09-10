class GameEngine:
    def __init__(self):
        self.board = [[None for i in range(3)] for i in range(3)]
        self.player = 'X'
        self.nextMove = None
        #print("Game Engine init")

    def changePlayer(self):
        if self.player == 'X':
            self.player = '0'
        else:
            self.player = 'X' 

    # If the move is valid the function retruns the updated board.
    # If the move is invalid the function returns None. 
    def makeMove(self, row, col, player):
        if (self.board[row][col] == None):
            self.board[row][col] = player
            #self.changePlayer()
            return self.board
        return None

    def nextState(self, row, col, player):
        if (self.board[row][col] == None):
            # makes a copy of the board 
            copy = self.board[:]
            # updates the copy with the given move
            copy[row][col] = player
            return copy
        return self.board[:]

    def printBoard(self):
        print(self.board)
        
    def minimax(self, board):
        # if the game has reached a terminal state
        winner = self.checkGameOver(board)
        if (winner == 'X'):
           return 1
        elif (winner == 'O'):
            return -1 
        elif (winner == '-'):
            return 0
        # otherwise 
        scores = []
        moves = []
        for move in self.getPossibleMoves(board):
            possibleGame = self.nextState(move[0], move[1])
            scores.append(self.minimax(possibleGame))
            moves.append(move)
        
        if self.player == 'X':
            maxScoreIdx = scores.index(max(scores))
            self.nextMove = moves[maxScoreIdx]
            return max(scores)
        else:
            minScoreIdx = scores.index(min(scores))
            self.nextMove = moves[minScoreIdx]
            return min(scores)

    
    # Returns the winning player if there is one. If there is a tie returns '-'. Otherwise None.
    def checkGameOver(self, board):
        # check win on straigh lines
        for i in range(0,3): 
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
        if self.getPossibleMoves == []:
            return '-' 

        return None

    def getPossibleMoves(self, board):
        possibleMoves = []
        for rowIdx, row in enumerate(board):
            for colIdx, column in enumerate(row):
                if column == None:
                    possibleMoves.append((rowIdx, colIdx))
                else:
                    pass
        return possibleMoves    

if __name__ == '__main__':
    g = GameEngine()
    g.printBoard()
    g.makeMove(0,0,1)
    g.makeMove(0,1,1)
    #print(g.checkVictory(g.board, 0, 1))
    g.makeMove(0,2,1)
    #print(g.checkVictory(g.board, 0, 2))
    print(g.getPossibleMoves(g.board))
    g.printBoard()
    #print(g.minimax(g.board))
    print("Run")