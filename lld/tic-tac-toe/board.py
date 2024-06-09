import random
class Board:
    board = None
    winner = None
    def __init__(self) -> None:
        self.board = self.initBoard()
    
    def initBoard(self):
        board = []
        for i in range(3):
            board.append(['_','_','_'])
        return board
    
    def validateMove(self, cellX, cellY):
        return cellX >=0 and cellX < 3 and cellY >= 0 and cellY < 3 and self.board[cellX][cellY] == '_'
        
                
    def makeMove(self, currentPlayer, cellX, cellY):
        move = Move(cellX, cellY, currentPlayer.piece)
        self.board[move.X][move.Y] = move.piece.value
        if self.checkWinner(currentPlayer.piece.value):
            self.winner = currentPlayer
        return move
        
    def checkWinner(self, piece):
        res = False
        # rowCheck
        for i in range(3):
            res |= self.board[i][0] == piece \
        and self.board[i][0] == self.board[i][1] \
        and self.board[i][1] == self.board[i][2]
        
        # colCheck
        for i in range(3):
            res |= self.board[0][i] == piece \
        and self.board[0][i] == self.board[1][i] \
        and self.board[1][i] == self.board[2][i]
        
        # diagonalCheck
        res |= self.board[0][0] == piece \
        and self.board[0][0] == self.board[1][1] \
        and self.board[1][1] == self.board[2][2]
        
        # reverseDiagonalCheck
        res |= self.board[0][2] == piece \
        and self.board[0][2] == self.board[1][1] \
        and self.board[1][1] == self.board[2][0]

        return res
    
    def getWinner(self):
        return self.winner
    
    def printBoard(self):
        # print(len(self.board))
        for i in range(3):
            for j in range(3):
                print(f"| {self.board[i][j]} |", end = "")
            print()

class Move:
    X = None
    Y = None
    piece = None
    
    def __init__(self, X, Y, piece) -> None:
        self.X = X
        self.Y = Y
        self.piece = piece