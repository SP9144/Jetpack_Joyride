import os
import time
from colorama import init, Fore, Back, Style

import config
from person import mando, boss_enemy
from object import scenery, cloud, coin1, beam_horizontal, beam_vertical, beam_diagonal, magnet
from board import board

# ================= set-up board =====================

obj_board = board(40, 400)
obj_board.initialize_board()

# ================= set-up scenery =====================

obj_scenery = scenery()
obj_scenery.create_ground(obj_board.get_grid())
obj_scenery.create_sky(obj_board.get_grid())

# ================= set-up objects =====================

grid = obj_board.get_grid()
cloud_pos = config.cloud_pos

for elm in cloud_pos:
    c = int(elm[1])
    d = int(elm[0])
    obj_cloud = cloud(c, d, 3, 6)
    shape = obj_cloud.get_shape()
    for i in range(3):
        for j in range(6):
            grid[c][d] = shape[i][j]
            d+=1
        d = int(elm[0])
        c+=1

coin1_pos = config.coin1_pos

for elm in coin1_pos:
    c = int(elm[1])
    d = int(elm[0])
    obj_coin1 = coin1(c, d, 2, 3)
    shape = obj_coin1.get_shape()
    for i in range(2):
        for j in range(3):
            grid[c+i][d+j] = shape[i][j]
        #     d+=1
        # d = int(elm[0])
        # c+=1

beam_ver_pos = config.beam_ver_pos

for elm in beam_ver_pos:
    c = int(elm[1])
    d = int(elm[0])
    obj_bv = beam_vertical(c, d, 3, 1)
    shape = obj_bv.get_shape()
    for i in range(3):
        for j in range(1):
            grid[c+i][d+j] = shape[i][j]
        #     d+=1
        # d = int(elm[0])
        # c+=1

beam_hor_pos = config.beam_hor_pos

for elm in beam_hor_pos:
    c = int(elm[1])
    d = int(elm[0])
    obj_bh = beam_horizontal(c, d, 1, 3)
    shape = obj_bh.get_shape()
    for i in range(1):
        for j in range(3):
            grid[c][d] = shape[i][j]
            d+=1
        d = int(elm[0])
        c+=1

beam_dgn_pos = config.beam_dgn_pos

for elm in beam_dgn_pos:
    c = int(elm[1])
    d = int(elm[0])
    obj_bd = beam_diagonal(c, d, 3, 3)
    shape = obj_bd.get_shape()
    for i in range(3):
        for j in range(3):
            grid[c][d] = shape[i][j]
            d+=1
        d = int(elm[0])
        c+=1

switch_boost = 1
switch_shield = 1

# ================= set-up obj_mando =====================

obj_mando = mando(28, 5, 3, 3)
# obj_mando.birth(grid)

def move_mando(option):

    [x, y] = obj_mando.get_pos()
    if option == 'q':
            # os.system('clear')
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT + username + ", YOU QUIT.")
            print(Style.RESET_ALL)
            exit()
    
    elif option == 'd':
        y += 2

    elif option == 'a':
        y -= 2        
        if(y<=3):
            y = 3

    elif option == 'w':
        x -= 4
        if(x<=4):
            x = 4
    
    obj_mando.change_pos(x, y+1)

    obj_mando.gravity(1)

# ================= set-up magnet =====================

mgn_pos = config.mgn_pos
obj_mgn = magnet(235, 20, 5, 3)

def print_mgn():
    for elm in mgn_pos:
        c = int(elm[1])
        d = int(elm[0])
        obj_mgn = magnet(c, d, 5, 3)
        shape = obj_mgn.get_shape()
        for i in range(5):
            for j in range(3):
                grid[c][d] = shape[i][j]
                d+=1
            d = int(elm[0])
            c+=1

def check_magnet():
    [w, h] = obj_mgn.get_objdim()
    [ymgn, xmgn] = obj_mgn.get_objpos()
    [x, y] = obj_mando.get_pos()

    # print(xmgn, ymgn)
    # print(x, y)
    # print(h/2, w/2)

    xmgn = xmgn + round(h/2)
    ymgn = ymgn + round(w/2)

    diffx = abs(x - (xmgn + round(h/2)))


    if((ymgn - round(w/2) - 20)  <= y <= (ymgn - round(w/2)) and diffx <= 20):
        y += 1
        if(x > xmgn):
            x -= 2
        else:
            x += 2
    if((ymgn + round(w/2))  <= y <= (ymgn - round(w/2) + 20) and diffx <= 20):
        y -= 1
        if(x > xmgn):
            x -= 2
        else:
            x += 2
    if( (ymgn - round(w/2)) <= y <= (ymgn + round(w/2)) ):
        if(x > xmgn):
            x -= 3
        else:
            x += 3

    obj_mando.change_pos(x, y) 

# ================= set-up boss_enemy =====================

obj_enemy = boss_enemy(17, 381, 10, 17)

def check_Mando_Boss():
    [x, y] = obj_mando.get_pos()
    [xboss, yboss] = obj_enemy.get_pos()

    if(yboss - y <= 100):
        obj_enemy.change_pos(x-5)

def dragon_bullets():
        obj_enemy.fire_bullets(grid)
        obj_enemy.move_bullets(grid)
# ================= check bullet and obs collision =====================

def check_bull_beam():
    beam_ver_pos = config.beam_ver_pos

    for elm in beam_ver_pos:
        flag = 0
        c = int(elm[1])
        d = int(elm[0])
        for i in range(3):
            for j in range(1):
                if(grid[c+i][d+j] == (Fore.WHITE + Style.BRIGHT + "*" + Fore.RESET + Style.RESET_ALL)):
                    flag = 1
        if(flag == 1):
            # print("HI")
            obj_mando.set_score(obj_mando.get_score()+1)
            for i in range(3):
                for j in range(1):
                    print("FY")
                    grid[c+i][d+j] = "f"
            

    beam_hor_pos = config.beam_hor_pos

    for elm in beam_hor_pos:
        flag = 0
        c = int(elm[1])
        d = int(elm[0])
        for i in range(1):
            for j in range(3):
                if(grid[c+i][d+j] == Fore.WHITE + Style.BRIGHT + "*" + Fore.RESET + Style.RESET_ALL):
                    flag = 1
        if(flag == 1):
            # print("HI")
            obj_mando.set_score(obj_mando.get_score()+1)
            for i in range(1):
                for j in range(3):
                    grid[c+i][d+j] = " "
    
    beam_dgn_pos = config.beam_dgn_pos

    for elm in beam_dgn_pos:
        flag = 0
        c = int(elm[1])
        d = int(elm[0])
        for i in range(3):
            for j in range(3):
                if(grid[c+i][d+j] == Fore.WHITE + Style.BRIGHT + "*" + Fore.RESET + Style.RESET_ALL):
                    flag = 1
        if(flag == 1):
            # print("HI")
            obj_mando.set_score(obj_mando.get_score()+1)
            for i in range(3):
                for j in range(3):
                    grid[c+i][d+j] = " "

# ================= MAIN =====================

if __name__ == '__main__':
    os.system('clear')
    config.intro()
    print(Fore.CYAN + "ENTER YOUR NAME: " + Fore.RESET)
    username = input()
    os.system('clear')
    
    start = time.time()

    while(True): # MAIN LOOP
        
        os.system('clear')

        actual_time = round(time.time()) - round(start)
        time_remain = 150 - (actual_time)

        config.header()
        print("Time Remaining: ", time_remain, end = '\t \t')
        print("Lives: ", obj_mando.get_lives(), end = '\t \t')
        print("Coins: ", obj_mando.get_coins(), end = '\t \t')
        print("Score: ", obj_mando.get_score())
        print("Boss Enemy Lives: ", obj_enemy.get_lives(), end = '\t \t')

        # Boost Working
        
        if(obj_mando.get_boost() == 1 and (round(time.time()) - obj_mando.get_booststartT()) <= 10):
            [x, y] = obj_mando.get_pos()
            print("Boost: ", "On" if obj_mando.get_boost() == 1 else "Off", end = '\t \t')
            print("Boost Time Remaining: ", 10 - (round(time.time()) - obj_mando.get_booststartT()), end = '\t \t')
            if(10 - (round(time.time()) - obj_mando.get_booststartT()) == 0):
                obj_mando.set_boosttimer(round(time.time()))
            obj_mando.change_pos(x, y+4)
            switch_boost = 1
        elif(obj_mando.get_boost() == 1 and (round(time.time()) - obj_mando.get_booststartT()) > 10):
            # print(round(time.time()), obj_mando.get_booststartT())
            obj_mando.set_boost(0)
            print("Boost: ", "On" if obj_mando.get_boost() == 1 else "Off", end = '\t \t')
            # obj_mando.set_boosttimer(round(time.time()))
            switch_boost = 1
        elif(obj_mando.get_boost() == 0 and (round(time.time()) - obj_mando.get_boosttimer()) <= 60):
            # print(round(time.time()), obj_mando.get_boosttimer())
            obj_mando.set_boost(0)
            print("Next boost in: ", 60 - (round(time.time()) - obj_mando.get_boosttimer()), end = '\t \t')
            switch_boost = 0
            # obj_mando.set_boosttimer(round(time.time()))
        elif(obj_mando.get_boost() == 0 and obj_mando.get_boosttimer()!=0):
            print("Boost: ", "On" if obj_mando.get_boost() == 1 else "Off", end = '\t \t')
            switch_boost = 1
        else:
            print("Boost: ", "On" if obj_mando.get_boost() == 1 else "Off", end = '\t \t')
            
        # Shield Working
        
        if(obj_mando.get_shield() == 1 and (round(time.time()) - obj_mando.get_shieldstartT()) <= 10):
            [x, y] = obj_mando.get_pos()
            print("Shield: ", "On" if obj_mando.get_shield() == 1 else "Off", end = '\t \t')
            print("Shield Time Remaining: ", 10 - (round(time.time()) - obj_mando.get_shieldstartT()), end = '\t \t')
            if(10 - (round(time.time()) - obj_mando.get_shieldstartT()) == 0):
                obj_mando.set_shieldtimer(round(time.time()))
            switch_shield = 1
        elif(obj_mando.get_shield() == 1 and (round(time.time()) - obj_mando.get_shieldstartT()) > 10):
            # print(round(time.time()), obj_mando.get_shieldstartT())
            obj_mando.set_shield(0)
            print("Shield: ", "On" if obj_mando.get_shield() == 1 else "Off", end = '\t \t')
            # obj_mando.set_shieldtimer(round(time.time()))
            switch_shield = 1
        elif(obj_mando.get_shield() == 0 and (round(time.time()) - obj_mando.get_shieldtimer()) <= 60):
            # print(round(time.time()), obj_mando.get_shieldtimer())
            obj_mando.set_shield(0)
            print("Next shield in: ", 60 - (round(time.time()) - obj_mando.get_shieldtimer()), end = '\t \t')
            switch_shield = 0
            # obj_mando.set_shieldtimer(round(time.time()))
        elif(obj_mando.get_shield() == 0 and obj_mando.get_shieldtimer()!=0):
            print("Shield: ", "On" if obj_mando.get_shield() == 1 else "Off", end = '\t \t')
            switch_shield = 1
        else:
            print("Shield: ", "On" if obj_mando.get_shield() == 1 else "Off", end = '\t \t')
        
        print()


        if(time_remain <= 0):
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT + username + " ,YOUR TIME IS UP.")
            print(Style.RESET_ALL)
            break

        if(obj_mando.get_lives() <= 0):
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT + username + " ,YOU LOST.")
            print(Style.RESET_ALL)
            break

        if(obj_enemy.get_lives() <= 0):
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT + username + " ,YOU WIN.")
            print(Style.RESET_ALL)
            break
        
        [x, y] = obj_mando.get_pos()
        if(y == 396):
            print(Fore.CYAN + Back.BLACK + Style.BRIGHT + username + " ,YOU WIN.")
            print(Style.RESET_ALL)
            break
        
        if(actual_time % 5 ==0):
            dragon_bullets()
        
        check_bull_beam()
        obj_mando.move_bullets(grid)
        
        print_mgn()
        check_magnet()

        grid=obj_board.get_grid()
        obj_mando.birth(grid) # coins and collisions checked too

        check_Mando_Boss()
        obj_enemy.birth(grid)

        [x, y] = obj_mando.get_pos()
        obj_board.print_board(y)

        key = config.input()

        grid=obj_board.get_grid()
        obj_mando.death(grid)
        obj_enemy.death(grid)
        obj_board.set_grid(grid)
        
        move_mando(key)

        if (key == ' ' and switch_shield):
            obj_mando.set_shield(1)
            obj_mando.set_shieldstartT(round(time.time()))
        elif (key == 'k' and switch_boost):
            obj_mando.set_boost(1)
            obj_mando.set_booststartT(round(time.time()))
            # print(obj_mando.get_booststartT())
        elif (key == 'b'):
            obj_mando.fire_bullets(grid)

        # time.sleep(0.1)

    