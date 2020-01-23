import sys
import time
import os

import config
from colorama import Fore, Back, Style


class person:
    def __init__(self, x, y, height, width):
        self._x= x
        self._y = y
        self._height = height
        self._width = width
        self._figure = []

    def birth(self, grid):
        self.check_collisions(grid)
        # print(self._y, self._y + self._width, self._x, self._x + self._height)
        for i in range(self._x, self._x + self._height, 1):
            for j in range(self._y, self._y + self._width, 1):
                grid[i][j] = self._figure[i-self._x][j-self._y]

    def death(self, grid):
        for i in range(self._x, self._x + self._height, 1):
                for j in range(self._y, self._y + self._width, 1):
                    grid[i][j] = " "

    def get_pos(self):
        return [self._x, self._y]

    def change_pos(self, x, y):
        if(x >= 34):
            x = 34
        if(x <= 4):
            x = 4
        if(y <= 3):
            y = 3
        if(y >= 377):
            y = 377
        self._x = x
        self._y = y
       
class mando(person):
    def __init__(self, x, y, height, width):    
        super().__init__(x, y, height, width)
        self._height = 3
        self._width = 3
        self.__lives = 5
        self.__score = 0
        self.__coins = 0
        self.__shield = 0
        self.shield_startT = 0
        self.__shieldtimer = 0
        self.__boost = 0
        self.boost_startT = 0
        self.__boosttimer = 0
        self.__bullets = []
        self._figure = [
            ["\\", "M", "/"],
            [" ", "|", " "],
            ["/", " ", "\\"]
        ]
        self._shieldfigure = [
            ["\\", "M", "/"],
            [" ", "|", " "],
            ["/", " ", "\\"]
        ]
        for i in range(self._height):
            for j in range(self._width):
                if self._figure[i][j] is "\\" or self._figure[i][j] is "M"or self._figure[i][j] is "/":
                    self._figure[i][j] = Fore.MAGENTA + self._figure[i][j] + Fore.RESET
                else:
                    self._figure[i][j] = Fore.WHITE + self._figure[i][j] + Fore.RESET
        for i in range(self._height):
            for j in range(self._width):
                if self._shieldfigure[i][j] is "\\" or self._shieldfigure[i][j] is "M"or self._shieldfigure[i][j] is "/":
                    self._shieldfigure[i][j] = Fore.MAGENTA + Back.YELLOW + Style.BRIGHT + self._shieldfigure[i][j] + Fore.RESET + Back.RESET + Style.RESET_ALL
                else:
                    self._shieldfigure[i][j] = Fore.WHITE + Back.YELLOW + Style.BRIGHT + self._shieldfigure[i][j] + Fore.RESET + Back.RESET + Style.RESET_ALL
        
    def get_lives(self):
        return self.__lives
    def set_lives(self, life_remain):
        self.__lives = life_remain

    def get_score(self):
        return self.__score
    def set_score(self, score_new):
        self.__score = score_new

    def get_coins(self):
        return self.__coins
    def set_coins(self, coin_new):
        self.__coins = coin_new

    def get_boost(self):
        return self.__boost
    def set_boost(self, switch):
        self.__boost = switch

    def get_booststartT(self):
        return self.__booststartT
    def set_booststartT(self, t):
        self.__booststartT = t
    
    def get_boosttimer(self):
        return self.__boosttimer
    def set_boosttimer(self, t):
        self.__boosttimer = t
    
    def get_shield(self):
        return self.__shield
    def set_shield(self, switch):
        self.__shield = switch

    def get_shieldstartT(self):
        return self.__shieldstartT
    def set_shieldstartT(self, t):
        self.__shieldstartT = t
    
    def get_shieldtimer(self):
        return self.__shieldtimer
    def set_shieldtimer(self, t):
        self.__shieldtimer = t

    def gravity(self, switch):
        if(switch == 1):
            self._x += 2
            if(self._x >= 34):
                self._x = 34

    def birth(self, grid):
        self.check_coins(grid)
        if(self.__shield == 0):
            self.check_collisions(grid)
            # print(self.x, self._x+ self._width, self._y, self._y + self._height)
            for i in range(self._x, self._x + self._height, 1):
                for j in range(self._y, self._y + self._width, 1):
                    grid[i][j] = self._figure[i-self._x][j-self._y]
        else:
            for i in range(self._x, self._x + self._height, 1):
                for j in range(self._y, self._y + self._width, 1):
                    grid[i][j] = self._shieldfigure[i-self._x][j-self._y]
            
    def check_coins(self, grid):
        # [x, y] = [self._x, self._y]

        # for i in [x-1, x+4]:
        #     for j in range(y-1, y+4):
        #         if(grid[i][j] == Fore.YELLOW + "$" + Fore.RESET):
        #             self.__coins += 1

        # for i in range(x, x+4):
        #     for j in [y-1, y+3]:
        #         if(grid[i][j] == Fore.YELLOW + "$" + Fore.RESET):
        #             self.__coins += 1   

        # print("coin", self.__coins, self._x, self._y, grid[self._x][self._y])     

        if(grid[self._x][self._y] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x][self._y + 1] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x][self._y + 2] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x + 1][self._y] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x + 1][self._y + 1] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x + 1][self._y + 2] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x + 2][self._y] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x + 2][self._y + 1] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1
        if(grid[self._x + 2][self._y + 2] == Fore.YELLOW + "$" + Fore.RESET):
            self.__coins += 1
            self.__score += 1

    def check_collisions(self, grid):
        if(grid[self._x][self._y] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x][self._y] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x][self._y + 1] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x][self._y+1] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x][self._y + 2] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x][self._y+2] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x + 1][self._y] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x+1][self._y] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x + 1][self._y + 1] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x+1][self._y+1] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x + 1][self._y + 2] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x+1][self._y+2] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x + 2][self._y] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x+2][self._y] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x + 2][self._y + 1] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x+2][self._y+1] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
        if(grid[self._x + 2][self._y + 2] == Fore.BLUE + Back.RED + "#" + Fore.RESET + Back.RESET or grid[self._x+2][self._y+2] == Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL):
            self.__lives -= 1
    
    def fire_bullets(self, grid):
        self.__bullets.append([self._x + 1, self._y + 5, 0])
        grid[self._x + 1][self._y + 5] = Fore.WHITE + Style.BRIGHT + "*" + Fore.RESET + Style.RESET_ALL

    def move_bullets(self, grid):
        
        for bullet in self.__bullets:
            x = bullet[0]
            y = bullet[1]
            bullet_dist = bullet[2]

            if(y >= 399 or bullet_dist == 30):
                grid[x][y] = " "
                continue
                        
            grid[bullet[0]][bullet[1]] = " "
            if(self.__boost == 1):
                bullet[1] +=3
                if(bullet[1] >= 399):
                    bullet[1] = 399
            elif(self.__boost == 0):
                bullet[1] +=2
                if(bullet[1] >= 399):
                    bullet[1] = 399
            grid[bullet[0]][bullet[1]] = Fore.WHITE + Style.BRIGHT + "*" + Fore.RESET + Style.RESET_ALL
            
            bullet[2] += 1

class boss_enemy(person):
    def __init__(self, x, y, height, width):    
        super().__init__(x, y, height, width)
        self._height = 10
        self._width = 17
        self.__lives = 5
        self.__bullets = []
        self._figure = [
            [" "," "," "," "," ","/"," "," "," "," "," ","\\"," "," "," "," "," "],
            [" "," "," "," ","(","("," "," "," "," "," ",")",")"," "," "," "," "],
            ["=","=","="," "," ","\\","\\","_","v","_","/","/"," "," ","=","=","="],
            [" "," ","=","=","=","=",")","_","^","_","(","=","=","=","="," "," "],
            [" "," ","=","=","=","/"," ","O"," ","O"," ","\\","=","=","="," "," "],
            [" "," ","="," ","|"," ","/","_"," ","_","\\"," ","|"," ","="," "," "],
            [" ","="," "," "," ","\\","/","_"," ","_","\\","/"," "," "," ","="," "],
            [" "," "," "," "," "," ","\\","_"," ","_","/"," "," "," "," "," "," "],
            [" "," "," "," "," "," ","(","o","_","o",")"," "," "," "," "," "," "],
            [" "," "," "," "," "," "," ","V","w","V"," "," "," "," "," "," "," "]
        ]
        for i in range(self._height):
            for j in range(self._width):
                if(self._figure[i][j] == "\\" or self._figure[i][j] == "/" or self._figure[i][j] == ")" or self._figure[i][j] == "(" or self._figure[i][j] == "|"):
                    self._figure[i][j] = Fore.GREEN + Style.BRIGHT + self._figure[i][j] + Fore.RESET + Style.RESET_ALL
                elif(self._figure[i][j] == "="):
                    self._figure[i][j] = Fore.BLUE + Style.BRIGHT + self._figure[i][j] + Fore.RESET + Style.RESET_ALL
                elif(self._figure[i][j] == "O"):
                    self._figure[i][j] = Fore.WHITE + Style.BRIGHT + self._figure[i][j] + Fore.RESET + Style.RESET_ALL
                elif(self._figure[i][j] == "_"):
                    self._figure[i][j] = Fore.YELLOW + Style.BRIGHT + self._figure[i][j] + Fore.RESET + Style.RESET_ALL
                elif(self._figure[i][j] == "V" or self._figure[i][j] == "w" or self._figure[i][j] == "^" or self._figure[i][j] == "v"):
                    self._figure[i][j] = Fore.RED + Style.BRIGHT + self._figure[i][j] + Fore.RESET + Style.RESET_ALL
                elif(self._figure[i][j] == "o"):
                    self._figure[i][j] = Fore.CYAN + Style.BRIGHT + self._figure[i][j] + Fore.RESET + Style.RESET_ALL

    def get_pos(self):
        return [self._x, self._y]

    def change_pos(self, x):
        if(x >= 27):
            x = 27
        if(x <= 4):
            x = 4
        self._x = x

    def fire_bullets(self, grid):
        self.__bullets.append([self._x + 7, self._y + 2, 0])
        grid[self._x + 5][self._y + 2] = Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL

    def move_bullets(self, grid):
        
        for bullet in self.__bullets:
            x = bullet[0]
            y = bullet[1]
            bullet_dist = bullet[2]

            if(y >= 399 or bullet_dist == 50):
                grid[x][y] = " "
                continue
                        
            grid[bullet[0]][bullet[1]] = " "

            bullet[1] -=3
            grid[bullet[0]][bullet[1]] = Fore.YELLOW + Style.BRIGHT + "o" + Fore.RESET + Style.RESET_ALL
            
            bullet[2] += 1

    def check_collisions(self, grid):
        for i in range(self._x, self._x + self._height, 1):
            for j in range(self._y, self._y + self._width, 1):
                if(grid[i][j] == Fore.WHITE + Style.BRIGHT + "*" + Fore.RESET + Style.RESET_ALL):
                    self.__lives -= 1

    def get_lives(self):
        return self.__lives
                
        
        

            
            


            
