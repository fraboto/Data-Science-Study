import os
import sys


def get_current_os():
    
    return sys.platform


def clear_console():

    if get_current_os() == 'win32':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    pass