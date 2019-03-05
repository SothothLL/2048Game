import random
from settings import *


def game_start():
    # 主循环
    global array, TIMES, score, screen
    # 屏幕
    screen = pygame.display.set_mode((screen_width, screen_height))
    # 设置标题
    pygame.display.set_caption('2048')
    # 初始化数组
    array = [[0 for i in range(size)] for i in range(size)]
    # 还有多少个空地方 最开始有16个空
    TIMES = size * size
    score = 0
    # 初始化两个数字方块
    create()
    create()
    # 显示游戏面板
    show_panel()

    while True:
        # 绘制背景图
        screen.blit(background_picture, (0, 0))
        if game_end():
            return
        # 时间循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 1
                else:
                    move_key(event)
        show_panel()


def game_over():
    # 游戏结束页面
    # 设置字体以及显示字体
    game_over_font = pygame.font.Font(game_font, 50)
    game_surf = game_over_font.render('Game Over', True, (255, 0, 0))
    # 获取当前字体所在矩形的长宽
    game_rect = game_surf.get_rect()
    # 设置矩形中心
    game_rect.center = (screen_width / 2, screen_height / 2)

    margin = pygame.Surface((screen_width, cell_size))
    margin.fill((255, 255, 255))
    game_restart_font = pygame.font.Font(game_font, 35)
    press_key_surf = game_restart_font.render('press R to restart', True, (0, 0, 0))
    press_key_rect = press_key_surf.get_rect()
    press_key_rect.center = (screen_width / 2, screen_height - 60)

    while True:
        # 设置背景图
        screen.blit(background_picture, (0, 0))
        screen.blit(game_surf, game_rect)
        screen.blit(margin, (0, screen_height - cell_size))
        screen.blit(press_key_surf, press_key_rect)
        # 时间循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 0
                elif event.key == pygame.K_ESCAPE:
                    return 1
        # 刷新
        pygame.display.update()


def move_key(event):
    # 判定键盘事件
    global score, TIMES, history
    # 标志整个二维数组是否发生了变化
    mark = False
    # 触发了向上的操作
    if event.key == pygame.K_w:
        for y in range(1, size):
            for x in range(0, size):
                if array[x][y] == 0:
                    continue
                # 标记位置 ,如果这个dispose一直为-1
                # 那么y以上的所有位置都不会被y代替的位置
                # 否则y1的位置将被y位置的元素代替
                dispose = -1
                for y1 in range(y - 1, -1, -1):
                    if array[x][y1] != 0:
                        if array[x][y] == array[x][y1]:
                            mark = True
                            dispose = -1
                            score += 2 * array[x][y1]
                            array[x][y1] *= 2
                            array[x][y] = 0
                            TIMES += 1
                        break
                    else:
                        dispose = y1
                # 不为-1的情况
                if dispose is not -1:
                    mark = True
                    change_y(x, y, dispose)
    # 触发了向下的操作
    if event.key == pygame.K_s:
        for y in range(size - 1, -1, -1):
            for x in range(0, 4):
                if array[x][y] == 0:
                    continue
                dispose = -1
                for y1 in range(y + 1, size):
                    if array[x][y1] != 0:
                        if array[x][y] == array[x][y1]:
                            mark = True
                            dispose = -1
                            score += 2 * array[x][y1]
                            array[x][y1] *= 2
                            array[x][y] = 0
                            TIMES += 1
                        break
                    else:
                        dispose = y1
                if dispose is not -1:
                    mark = True
                    change_y(x, y, dispose)
    # 触发了向左的操作
    if event.key == pygame.K_a:
        for y in range(0, size):
            for x in range(1, size):
                if array[x][y] == 0:
                    continue
                dispose = -1
                for x1 in range(x - 1, -1, -1):
                    if array[x1][y] != 0:
                        if array[x1][y] == array[x][y]:
                            mark = True
                            dispose = -1
                            score += 2 * array[x1][y]
                            array[x1][y] *= 2
                            array[x][y] = 0
                            TIMES += 1
                        break
                    else:
                        dispose = x1
                if dispose is not -1:
                    mark = True
                    change_x(x, y, dispose)
    # 触发了向右的操作
    if event.key == pygame.K_d:
        for y in range(0, size):
            for x in range(size - 1, -1, -1):
                if array[x][y] == 0:
                    continue
                dispose = -1
                for x1 in range(x + 1, size):
                    if array[x1][y] != 0:
                        if array[x1][y] == array[x][y]:
                            mark = True
                            dispose = -1
                            score += 2 * array[x1][y]
                            array[x1][y] *= 2
                            array[x][y] = 0
                            TIMES += 1
                        break
                    else:
                        dispose = x1
                if dispose is not -1:
                    mark = True
                    change_x(x, y, dispose)
    if mark:
        create()
    if score >= history:
        history = score


def change_y(x, y, dispose):

    array[x][dispose] = array[x][y]
    array[x][y] = 0


def change_x(x, y, dispose):
    array[dispose][y] = array[x][y]
    array[x][y] = 0


def create():
    # 在空方块处产生新的数字
    # 直到某个空位置产生一个新的数,mark变为0
    mark = False
    if TIMES > 0:
        while not mark:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            # print x,y
            if array[x][y] == 0:
                # 1/4的几率生成 4
                if random.randint(0, 3) == 0:
                    array[x][y] = 4
                else:
                    array[x][y] = 2
                mark = True


def game_end():
    # 判定游戏的结束状态
    for r in range(size):
        for c in range(size):
            if array[r][c] == 0:
                return False
    for r in range(size):
        for c in range(size - 1):
            if array[r][c] == array[r][c + 1]:
                return False
    for r in range(size - 1):
        for c in range(size):
            if array[r][c] == array[r + 1][c]:
                return False
    return True


def show_panel():
    # 显示游戏面板
    for i in range(size):
        for j in range(size):
            white = (255, 255, 255)
            # 画矩形
            outer_rect = pygame.Rect(cell_size * i, cell_size * j + 100, cell_size, cell_size)
            pygame.draw.rect(screen, white, outer_rect)
            inner_rect = pygame.Rect(cell_size * i + 5, cell_size * j + 100 + 5, cell_size - 10, cell_size - 10)
            if array[i][j] != 0:
                t = array[i][j]
                num = 0
                while t != 1:
                    num += 1
                    t /= 2
                # 绘制方块颜色
                pygame.draw.rect(screen, color[num % 14], inner_rect)
                rect_font = pygame.font.Font(game_font, 30)
                map_text = rect_font.render(str(array[i][j]), True, (0, 0, 0))
                text_rect = map_text.get_rect()
                text_rect.center = (cell_size * i + cell_size / 2, cell_size * j + cell_size / 2+100)
                screen.blit(map_text, text_rect)
            else:
                pygame.draw.rect(screen, color[0], inner_rect)
    # 绘制分数
    score_board(map_text)
    # 刷新屏幕
    pygame.display.update()


def score_board(map_text):
    # 绘制分数
    score_font = pygame.font.Font(game_font, 30)
    score_text = score_font.render("Score:%s" % str(score), True, (255, 255, 0))
    text_rect = map_text.get_rect()
    text_rect.center = (50, 35)
    screen.blit(score_text, text_rect)

    history_font = pygame.font.Font(game_font, 30)
    score_text = history_font.render("History:%s" % str(history), True, (255, 255, 0))
    text_rect = map_text.get_rect()
    text_rect.center = (screen_width/2+50, 35)
    screen.blit(score_text, text_rect)
