import pygame

# 屏幕宽高
screen_width = 480
screen_height = 580
# 分数区域的高度
score_height = screen_height - screen_width
# 块大小
cell_size = 120
# 每行以及每列的块数
size = 4
# 屏幕初始化
screen = pygame.display.set_mode((screen_width, screen_height))
# 背景图对象
background_picture = pygame.image.load('image/background.jpg').convert()
# 数字数组
array = [[0 for i in range(size)] for i in range(size)]
# 16个方块的Surface对象
block = [pygame.Surface((cell_size, cell_size)) for i in range(15)]
# 字体设置
game_font = 'font/msmono.ttf'
# RGB颜色待选数组
color = [
    (192, 192, 192),
    (211, 211, 211),
    (0, 255, 0),
    (255, 105, 180),
    (0, 0, 255),
    (255, 255, 0),
    (0, 0, 139),
    (119, 136, 153),
    (0, 206, 209),
    (0, 128, 128),
    (173, 255, 47),
    (255, 250, 205),
    (255, 215, 0),
    (255, 250, 240),
    (255, 239, 205)
]
for i in range(15):
    block[i].fill(color[i])
# 还有多少个空地方 最开始有16个空
TIMES = size * size
# 总分数
score = 0
# 历史分数
history = 0
