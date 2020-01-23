import os
import sys
import termios, tty, time

from colorama import init, Fore, Back, Style

columns = 100
rows = 40

coin1_pos = [
    (220, 20), (230, 15), (240, 15), (250, 20),  
    (272, 17), (282, 17), (292, 17), 
    (169, 24), (189, 15), (199, 26), 
    (125, 13), (135, 14), (145, 13), (155, 14),
    (86, 17), (106, 17),
    (16, 20), (26, 15), (36, 20), (46, 15), (56, 20)
]

cloud_pos = [
    (10, 6), (20, 4), (43, 6), (30, 6), (57, 4), (68, 6),
    (89, 6), (120, 4), (134, 6), (157, 6), (172, 4), (196, 6),
    (200, 6), (228, 4), (250, 6), (243, 6), (271, 4), (293, 6)
]

beam_ver_pos = [
    (96, 17), (76, 17), (116,17), (225, 20), (245, 20),
    (262, 17), (287, 17), (297, 17)
]

beam_hor_pos = [
    (125, 15), (135, 12), (145, 15), (155, 12),
    (26, 20), (36, 15), (46, 20), (234, 27), (250, 27)
]

beam_dgn_pos = [
    (67, 31), (92, 25), (130, 29), (192, 25), (222, 32)
]

mgn_pos = [
    (235, 20)
]


def header():
    print(Fore.RED + Back.BLACK + Style.BRIGHT + "JETPACK JOYRIDE".center(columns), end='')
    print(Style.RESET_ALL)

def intro():
    print(Fore.CYAN + Back.BLACK + "   $$$$$\           $$\                                   $$\                     $$$$$\                               $$\       $$\           ".center(columns))
    print(Fore.CYAN + Back.BLACK + "   \__$$ |          $$ |                                  $$ |                    \__$$ |                              \__|      $$ |          ".center(columns))
    print(Fore.CYAN + Back.BLACK + "      $$ | $$$$$$\$$$$$$\    $$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\                  $$ | $$$$$$\  $$\   $$\  $$$$$$\  $$\  $$$$$$$ | $$$$$$\  ".center(columns))
    print(Fore.CYAN + Back.BLACK + "      $$ |$$  __$$\_$$  _|  $$  __$$\  \____$$\ $$  _____|$$ | $$  |                 $$ |$$  __$$\ $$ |  $$ |$$  __$$\ $$ |$$  __$$ |$$  __$$\ ".center(columns))
    print(Fore.CYAN + Back.BLACK + "$$\   $$ |$$$$$$$$ |$$ |    $$ /  $$ | $$$$$$$ |$$ /      $$$$$$  /            $$\   $$ |$$ /  $$ |$$ |  $$ |$$ |  \__|$$ |$$ /  $$ |$$$$$$$$ |".center(columns))
    print(Fore.CYAN + Back.BLACK + "$$ |  $$ |$$   ____|$$ |$$\ $$ |  $$ |$$  __$$ |$$ |      $$  _$$<             $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |$$   ____|".center(columns))
    print(Fore.CYAN + Back.BLACK + "\$$$$$$  |\$$$$$$$\ \$$$$  |$$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\            \$$$$$$  |\$$$$$$  |\$$$$$$$ |$$ |      $$ |\$$$$$$$ |\$$$$$$$\ ".center(columns))
    print(Fore.CYAN + Back.BLACK + "\______/  \_______| \____/ $$  ____/  \_______| \_______|\__|  \__|            \______/  \______/  \____$$ |\__|      \__| \_______| \_______| ".center(columns))
    print(Fore.CYAN + Back.BLACK + "                           $$ |                                                                   $$\   $$ |                                   ".center(columns))
    print(Fore.CYAN + Back.BLACK + "                           $$ |                                                                   \$$$$$$  |                                   ".center(columns))
    print(Fore.CYAN + Back.BLACK + "                           \__|                                                                    \______/                                    ".center(columns) + Style.RESET_ALL)


# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:

    def __init__(self):
        self.impl = _GetchUnix()


    def __call__(self):
        return self.impl()


class _GetchUnix:


    def __init__(self):
        import tty, sys


    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


_getch = _Getch()

class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def input(timeout=0.5):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    #signal.alarm(timeout)
    signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


