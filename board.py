from colorama import Fore, Back

class board:
    def __init__(self, rows, columns):
        self.__rows = rows 
        self.__columns = columns 
        self.__grid = []

    # Get terminal size
    # columns = shutil.get_terminal_size().columns
    # rows = shutil.get_terminal_size().lines

    def get_grid(self):
        return self.__grid
    def set_grid(self,grid):
        self.__grid=grid

    def get_rows(self):
        return self.__rows
    
    def get_cols(self):
        return self.__columns
    

    def initialize_board(self):
        for i in range(self.__rows):
            row_array = []
            for j in range(self.__columns):
                row_array.append(" ")
            self.__grid.append(row_array)

        # Border of the board
        for j in range(1, self.__rows-1):
            self.__grid[j][0] = Fore.BLACK + Back.BLACK + "|" + Fore.RESET + Back.RESET
            
        # for i in range(self.__columns):
        #     self.__grid[0][i] = Fore.BLACK + " " + Fore.RESET
        #     self.__grid[self.__rows-1][i] = Fore.BLACK + " " + Fore.RESET

    def print_board(self, mando_coord):
        if(mando_coord >= 0 and mando_coord <=30):
            for i in range(self.__rows):
                for j in range(0, 100):
                    print(self.__grid[i][j], end='')
                print()
        elif(mando_coord >= self.__columns - 100):
            for i in range(self.__rows):
                for j in range(self.__columns - 100, self.__columns):
                    print(self.__grid[i][j], end='')
                print()
        else:
            for i in range(self.__rows):
                for j in range(mando_coord - 30, mando_coord + 70):
                    print(self.__grid[i][j], end='')
                print()

    
