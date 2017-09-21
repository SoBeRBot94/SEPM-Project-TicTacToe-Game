import copy
import sys
import ast 

class GameEngine:
    def __init__(self):
        self.board = [[None for i in range(3)] for i in range(3)]
        self.player = 'X'
        self.nextMove = None
        #print("Game Engine init")

    def changePlayer(self):
        if self.player == 'X':
            self.player = 'O'
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

    def printBoard(self):
        print('-----------')
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print('-----------')
        
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
           

class AI:
    
    def __init__(self):
        self.nextMove = None
    
    def emptyBoard(self):
        return [[None, None, None], [None, None, None], [None, None, None]]

    def optimalNextMove(self, board, currentPlayer = 'X'):
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'
        self._optimalNextMove(board, currentPlayer)
        return self.nextMove

    def _optimalNextMove(self, board, currentPlayer):
        if (self.isTerminalState(board)):
            return self.score(board)
        if (board == self.emptyBoard()):
            self.nextMove = (0,0)
            return 
        possibleMoves = self.getPossibleMoves(board)
        scores = []
        moves = []
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'
        for move in possibleMoves:
            possibleNewBoard = self.nextState(board, move, currentPlayer)
            score = self._optimalNextMove(possibleNewBoard, currentPlayer)
            moves.append(move)
            scores.append(score)
        
        if currentPlayer == 'X':
            maxScoreIdx = scores.index(max(scores))
            self.nextMove = moves[maxScoreIdx]
            return max(scores)
        else: 
            minScoreIdx = scores.index(min(scores))
            self.nextMove = moves[minScoreIdx]
            return min(scores)


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
        return copy.deepcopy(board)



if __name__ == '__main__':
    #g = GameEngine()
    #g.printBoard()
    #g.makeMove(0,0,1)
    #g.makeMove(0,1,1)
    #print(g.checkVictory(g.board, 0, 1))
    #g.makeMove(0,2,1)
    #print(g.checkVictory(g.board, 0, 2))
    #print(g.getPossibleMoves(g.board))
    #g.printBoard()
    #print(g.minimax(g.board))
    print("Run")
    ai = AI()
    ga = GameEngine()
    currentPlayer = 'X'
    #while not (ai.isTerminalState(ga.board)): 
    #    m1 = ai.optimalNextMove(ga.board, currentPlayer)
    #    ga.makeMove(m1[0], m1[1], currentPlayer)
    #    currentPlayer = 'O' if currentPlayer == 'X' else 'X'
    #    print(ga.board)
    while not (ai.isTerminalState(ga.board)):
        if (currentPlayer == 'O'): 
            m1 = ai.optimalNextMove(ga.board, currentPlayer)
            ga.makeMove(m1[0], m1[1], currentPlayer)
        else: 
            m2 = ast.literal_eval(input("nästa drag: "))
            ga.makeMove(m2[0], m2[1], currentPlayer)
        ga.printBoard()
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'
    #    print(ga.board)
    #print(ai.optimalNextMove([['X', 'X', None],['O', 'X', 'O'], [None, None, None]]))
    #print(ai.optimalNextMove([['X', 'O', 'O'],[None, 'O', 'X'], [None, 'X', None]]))
    #print(ai.optimalNextMove([["X", "O", "O"], ["O","O", "X"],[None, None, "X"]]))