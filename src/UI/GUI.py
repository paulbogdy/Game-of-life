import pygame
import time


class GUI:
    def __init__(self, board, height, width, dim):
        self.__stop = True
        self.__displacement_x = 0
        self.__displacement_y = 0
        self.__dim = dim
        self.__board = board
        self.__height = height
        self.__width = width
        self.__screen = pygame.display.set_mode((height, width))
        self.__buttons = []

    def __draw_board(self):
        self.__screen.fill((255, 255, 255))
        to_draw = self.__board.all
        for element in to_draw:
            i, j = element
            pygame.draw.rect(self.__screen, (0, 255, 0), (self.__displacement_x + self.__dim * i,
                                                          self.__displacement_y + self.__dim * j,
                                                          self.__dim, self.__dim))
        pygame.display.update()

    def __set_piece(self, pos):
        x = (pos[0] - self.__displacement_x) // self.__dim
        y = (pos[1] - self.__displacement_y) // self.__dim
        self.__board[(x, y)] = 1

    def run(self):
        running = True
        mouse_pos = None
        moved = False
        while running:
            if mouse_pos is not None:
                new_pos = pygame.mouse.get_pos()
                if new_pos != mouse_pos:
                    moved = True
                    self.__displacement_x += new_pos[0] - mouse_pos[0]
                    self.__displacement_y += new_pos[1] - mouse_pos[1]
                    mouse_pos = new_pos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    if not moved:
                        self.__set_piece(mouse_pos)
                    mouse_pos = None
                    moved = False
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__stop = not self.__stop
                    if event.key == pygame.K_EQUALS:
                        self.__dim += 1
                    if event.key == pygame.K_MINUS:
                        self.__dim -= 1
            if not self.__stop:
                self.__board.update()
            self.__draw_board()
            time.sleep(0.05)
