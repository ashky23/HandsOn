from game import TicTacToeGame, Piece
from player import Player

def main():
    # player 1
    playerA = Player(name = "A", age = 23, piece = Piece.ZERO)
    # player 2
    playerB = Player(name = "B", age = 32, piece = Piece.CROSS)
    ticTacToeGameInstance = TicTacToeGame(playerA=playerA, playerB=playerB)
    print(ticTacToeGameInstance.getGameStatus())
    print(ticTacToeGameInstance.printBoard())
    print(ticTacToeGameInstance.getWinner())
    ticTacToeGameInstance.startGame()
    print(ticTacToeGameInstance.getWinner())
    print(ticTacToeGameInstance.printMoves())
    print(ticTacToeGameInstance.printBoard())
    print(ticTacToeGameInstance.getGameStatus())

main()
