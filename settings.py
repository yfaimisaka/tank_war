import os
from pygame import Rect


class Settings:
    # 游戏设置
    FPS = 60  # 游戏帧率
    GAME_NAME = "坦克大战"  # 游戏标题
    BOX_SIZE = 50  # 单位屏幕大小
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)  # 单位屏幕矩形
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 19, BOX_SIZE * 13)  # 屏幕矩形
    SCREEN_COLOR = (0, 0, 0)  # 屏幕颜色

    # 通用变量
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    # 单人地图
    # 游戏类型的地图字典
    MAP_DICT = {
        "S": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
            [0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
            [0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
            [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, ],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
            [0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, ],
            [0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, ]],
        "D": [
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
            [0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, ],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, ],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
            [0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, ],
            [0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ]
    }

    # 音频
    BOOM_MUSIC = "resources/musics/boom.wav"
    FIRE_MUSIC = "resources/musics/fire.wav"
    HIT_MUSIC = "resources/musics/hit.wav"

    # 坦克类型
    HERO = 0
    ENEMY = 1

    # 我方坦克
    HERO_IMAGE_NAME = "./resources/images/hero/hero1U.gif"
    HERO_IMAGES = {
        LEFT: "./resources/images/hero/hero1L.gif",
        RIGHT: "./resources/images/hero/hero1R.gif",
        UP: "./resources/images/hero/hero1U.gif",
        DOWN: "./resources/images/hero/hero1D.gif"
    }
    HERO_SPEED = 2
    HERO_BOSS_IMAGE = "./resources/images/5.png"
    # 我方老家

    # 敌方坦克，双人模式
    ENEMY_IMAGE_NAME = "./resources/images/enemy/enemy1D.gif"
    ENEMY_IMAGES_DOUBLE = {
        LEFT: "./resources/images/enemy/enemy1L.gif",
        RIGHT: "./resources/images/enemy/enemy1R.gif",
        UP: "./resources/images/enemy/enemy1U.gif",
        DOWN: "./resources/images/enemy/enemy1D.gif"
    }
    ENEMY_SPEED_DOUBLE = 2
    ENEMY_BOSS_IMAGE = "./resources/images/5.png"
    # 敌方坦克,单人模式
    ENEMY_IMAGES_SINGLE = {
        LEFT: "./resources/images/enemy/enemy2L.gif",
        RIGHT: "./resources/images/enemy/enemy2R.gif",
        UP: "./resources/images/enemy/enemy2U.gif",
        DOWN: "./resources/images/enemy/enemy2D.gif"
    }
    ENEMY_SPEED_SINGLE = 1

    # 子弹
    BULLET_IMAGE_NAME = "./resources/images/bullet/bullet.png"
    BULLET_RECT = Rect(0, 0, 5, 5)
    BULLET_SPEED = 5

    # 0表示空白、1表示红墙、2表示铁墙、3表示草、4表示海、5表示鸟
    RED_WALL = 1
    IRON_WALL = 2
    WEED_WALL = 3
    HERO_BOSS_WALL = 5
    ENEMY_BOSS_WALL = 6
    WALLS = [
        f"resources/images/walls/{file}" for file in os.listdir("resources/images/walls/")
    ]

    # 爆炸的图片
    BOOMS = [
        "resources/images/boom/" + file for file in os.listdir("resources/images/boom")
    ]

    # 开始界面的文字和背景图
    DISPLAY_WIDTH = 1180
    DISPLAY_HEIGHT = 812
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (150, 150, 150)
    BG_IMG = "./resources/images/screen/tank.png"

    # 输了时的音乐
    OVER_MUS = "./resources/musics/over_music.wav"
    # 预备start bgm
    NEW_START = "./resources/musics/startbgm2.wav"

    # Init页背景图
    INIT_IMG = "./resources/images/init/tank.jpg"
