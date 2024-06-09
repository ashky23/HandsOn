import random
from board import Board
from enum import Enum


class TicTacToeGameStatus (Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    DRAW = "DRAW"

class Piece (Enum):
    ZERO = '0'
    CROSS = 'X'

class TicTacToeGame:
    playerA = None
    playerB = None
    board = None
    status = None
    currentPlayer = None
    moves = None
    
    def __init__(self, playerA = None, playerB = None) -> None:
        self.playerA = playerA
        self.playerB = playerB
        self.board = Board()
        self.status = TicTacToeGameStatus.NOT_STARTED.value
        self.moves = []
    
    def toss(self):
        return  random.choice([self.playerA, self.playerB])
    
    def startGame(self):
        print("Game Started!!\n")
        self.currentPlayer = self.toss()
        self.status = TicTacToeGameStatus.IN_PROGRESS.value
        while True:
            print(f"{self.currentPlayer} 's move")
            print("please input x")
            x = int(input())
            print("please input y")
            y = int(input())
            if not self.board.validateMove(cellX=x, cellY=y):
                print(f"invalid move for player {self.currentPlayer}\nTry Again!!!")
                continue
            move = self.board.makeMove(self.currentPlayer, x, y)
            self.moves.append(move)
            if self.getWinner() != None:
                self.status = TicTacToeGameStatus.COMPLETED.value
                break
            if len(self.moves) == 9:
                print("Game Draw!!!")
                self.status = TicTacToeGameStatus.DRAW.value
                break
            self.printBoard()
            self.changePlayer()
        print("Game Ended!!\n")
            
    def changePlayer(self):
        if self.currentPlayer == self.playerA:
            self.currentPlayer = self.playerB
        else :
            self.currentPlayer = self.playerA
    
    def getWinner(self):
        return self.board.getWinner()
    
    def getGameStatus(self):
        return self.status
    
    def printMoves(self):
        print("Here are the moves of the game")
        for move in self.moves:
            print(f"{move.X}, {move.Y} --> {move.piece}")
    
    def printBoard(self):
        self.board.printBoard()