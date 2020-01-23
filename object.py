import os
from colorama import Fore, Back

import config

class scenery:

    def create_ground(self, grid):
            for i in range(400):
                grid[config.rows-3][i] = Fore.GREEN + "T" + Fore.RESET
                grid[config.rows-2][i] = Fore.GREEN + Back.GREEN + "T" + Fore.RESET + Back.RESET

    def create_sky(self, grid):
        for i in range(400):
            grid[1][i] = Fore.CYAN + Back.CYAN + "X" + Fore.RESET + Back.RESET
            grid[2][i] = Fore.CYAN + "X" + Fore.RESET

class object:

    def __init__(self, x, y, height, width):
        self._x = x
        self._y = y
        self._height = height
        self._width= width
        self._shape = []

    def get_shape(self):
        return self._shape

    def get_objpos(self):
        return [self._x, self._y]

    def get_objdim(self):
        return [self._height, self._width]

class cloud(object):

    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self._height = 3
        self._width= 6
        self._shape = [ 
            [" ", "(", "-", "-", ")", " "], 
            ["(", "-", "~", "-", "~", ")"], 
			[" ", "(", "-", "-", ")", " "] 
        ]
        for i in range(self._height):
            for j in range(self._width):
                self._shape[i][j] = Fore.BLUE + self._shape[i][j] + Fore.RESET

class coin1(object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self._height = 2
        self._width= 3
        self._shape = [
            ["$", "$", "$"],
            ["$", "$", "$"],
        ]
        for i in range(self._height):
            for j in range(self._width):
                self._shape[i][j] = Fore.YELLOW + self._shape[i][j] + Fore.RESET

class beam_horizontal(object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self._height = 1
        self._width= 3
        self._shape = [
            ["#", "#", "#"],
        ]
        for i in range(self._height):
            for j in range(self._width):
                self._shape[i][j] = Fore.BLUE + Back.RED + self._shape[i][j] + Fore.RESET + Back.RESET

class beam_vertical(object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self._height = 3
        self._width= 1
        self._shape = [
            ["#"],
            ["#"],
            ["#"]
        ]
        for i in range(self._height):
            for j in range(self._width):
                self._shape[i][j] = Fore.BLUE + Back.RED + self._shape[i][j] + Fore.RESET  + Back.RESET

class beam_diagonal(object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self._height = 3
        self._width= 3
        self._shape = [
            ["#", " ", " "],
            [" ", "#", " "],
            [" ", " ", "#"],
        ]
        for i in range(self._height):
            for j in range(self._width):
                if(self._shape[i][j] == "#"):
                    self._shape[i][j] = Fore.BLUE + Back.RED + self._shape[i][j] + Fore.RESET  + Back.RESET

class magnet(object):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
        self._height = 5
        self._width= 3
        self._shape = [
            ["  ", "___", "  "],
            ["  ", "___", "  "],
            ["/ /", "  ", "\\ \\"],
            ["| |", "  ", "| |"],
            ["| |", "  ", "| |"],
        ]
        self._shape[4][0] = Fore.RED + Back.RED + self._shape[4][0] + Fore.RESET + Back.RESET
        self._shape[4][2] = Fore.BLUE  + Back. BLUE + self._shape[4][2] + Fore.RESET + Back.RESET
        for i in range(self._height):
            for j in range(self._width):
                if(i != 4 and j != 0 or i != 4 and j != 2 or self._shape[i][j] != "  "):
                    self._shape[i][j] = Fore.WHITE + self._shape[i][j] + Fore.RESET 

# class speed_boost(object):
#     def __init__(self, x, y, height, width):
#         super().__init__(x, y, height, width)
#         self._height = 3
#         self._width= 3
#         self._shape = [
#             ["-", "----", "-"],
#             ["-", ">>>>", "-"],
#             ["-", "----", "-"]
#         ]
#         self._shape[1][1] = Fore.YELLOW + Back.BLACK + self._shape[1][1] + Fore.RESET + Back.RESET
#         for i in range(self._height):
#             for j in range(self._width):
#                 if(self._shape[i][j] != Fore.YELLOW + Back.BLACK + ">>>>" + Fore.RESET + Back.RESET):
#                     self._shape[i][j] = Fore.RED + Back.RED + self._shape[i][j] + Fore.RESET  + Back.RESET
        
            
            



