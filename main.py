from src.UI.Console import Console
from src.Boards.Board import Board, SparseBoard
from src.UI.GUI import GUI


if __name__ == '__main__':
    board = SparseBoard()
    board.load("glider_gun.txt")
    gui = GUI(board, 1560, 720, 16)
    gui.run()
