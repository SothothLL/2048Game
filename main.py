import game_function as gf
from settings import *

pygame.init()


def main():
    while True:
        if gf.game_start() == 1:
            return
        if gf.game_over():
            return


if __name__ == '__main__':
    main()
