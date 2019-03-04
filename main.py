import game_function as gf
from settings import *


# 游戏初始化
pygame.init()


def main():
    # 开始游戏
    while True:
        if gf.game_start() == 1:
            return
        if gf.game_over():
            return


if __name__ == '__main__':
    main()
