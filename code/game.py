#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, MENU_OPTION
from code.const import WIN_HEIGHT
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()
            print("Menu return = ", menu_return)

            if menu_return == 4:
                print("MENU_OPTION = 4")
                pygame.quit()
                quit()
            elif menu_return in [0, 1, 2]:
                print("MENU_OPTION = 0, 1, 2")
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
            else:
                pass
