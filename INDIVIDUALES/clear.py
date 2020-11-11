import os
import sys


def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


if __name__ == '__main__':
    print('hola')

    clear()
