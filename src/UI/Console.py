import os
import sys
import curses
import time


class Console:
    def __init__(self, board):
        self.__board = board
        pass

    def run(self):
        my_window = curses.initscr()
        while True:
            self.__board.update_board()
            my_window.refresh()
            time.sleep(1)
