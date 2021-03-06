import pygame
from sprites import *
from tank_war import TankWar
from common import Common


class TankWarSingle(TankWar):

    def __init__(self):
        super(TankWarSingle, self).__init__()
        self.enemies = None
        self.enemy_bullets = None
        self.enemies_life = True
        with open("settings", "r") as f:
            self.enemy_count = int(f.read())
        with open("privacy", "r") as f1:
            self.username = f1.read()

    def create_sprite(self, game_type):
        """
        创建单人模式下精灵
        包括英雄和随机个敌人
        """
        self.hero = HeroOrEnemy(Settings.HERO_IMAGE_NAME, self.screen, Settings.HERO)
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for i in range(self.enemy_count):
            direction = random.randint(0, 3)
            enemy = Enemy(Settings.ENEMY_IMAGES_SINGLE[direction], self.screen)
            enemy.direction = direction
            self.enemies.add(enemy)
        super(TankWarSingle, self).draw_map(game_type)

    def check_keydown(self, event):
        """检查按下按钮的事件"""
        if event.key == pygame.K_LEFT:
            # 按下左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_RIGHT:
            # 按下右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_UP:
            # 按下上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_DOWN:
            # 按下下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_1:
            # 坦克发子弹
            self.hero.shot()

    def check_keyup(self, event):
        """检查松开按钮的事件"""
        if event.key == pygame.K_LEFT:
            # 松开左键
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = False
        elif event.key == pygame.K_RIGHT:
            # 松开右键
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = False
        elif event.key == pygame.K_UP:
            # 松开上键
            self.hero.direction = Settings.UP
            self.hero.is_moving = False
        elif event.key == pygame.K_DOWN:
            # 松开下键
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = False

    def event_handler(self):
        for event in pygame.event.get():
            # 判断是否是退出游戏
            if event.type == pygame.QUIT:
                Common.game_over()
            elif event.type == pygame.KEYDOWN:
                TankWarSingle.check_keydown(self, event)  # ????为什么不能写self，会爆event 是Unexpected argument
            elif event.type == pygame.KEYUP:
                TankWarSingle.check_keyup(self, event)

    def check_collide(self):
        # 保证坦克不移出屏幕
        self.hero.hit_wall()
        for enemy in self.enemies:
            enemy.hit_wall_turn()

        # 子弹击中墙
        for wall in self.walls:
            # 我方英雄子弹击中墙
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Settings.HERO_BOSS_WALL:
                        self.hero.kill()
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()
            # 敌方英雄子弹击中墙
            for enemy in self.enemies:
                for bullet in enemy.bullets:
                    if pygame.sprite.collide_rect(wall, bullet):
                        if wall.type == Settings.RED_WALL:
                            wall.kill()
                            bullet.kill()
                        elif wall.type == Settings.HERO_BOSS_WALL:
                            self.hero.kill()
                        elif wall.type == Settings.IRON_WALL:
                            bullet.kill()

            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.hero, wall):
                # 不可穿越墙
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.HERO_BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # 移出墙内
                    self.hero.move_out_wall(wall)

            # 敌方坦克撞墙
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.HERO_BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        # 子弹击中敌人，子弹和敌人都消失， 不用这个方法，无法计数
        # pygame.sprite.groupcollide(self.player2.bullets, self.enemies, True, True)

        # 当敌人数量为0时，敌人life为False
        for enemy in self.enemies:
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(bullet, enemy):
                    enemy.kill()
                    bullet.kill()
                    self.enemy_count -= 1

        # 敌方子弹击中我方
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if pygame.sprite.collide_rect(bullet, self.hero):
                    bullet.kill()
                    self.hero.kill()

    def update_sprites(self):
        # 监听
        if not self.enemy_count:
            self.enemies_life = False
        if self.hero.is_moving:
            self.hero.update()
        self.walls.update()
        self.hero.bullets.update()
        self.enemies.update()
        for enemy in self.enemies:
            enemy.bullets.update()
            enemy.bullets.draw(self.screen)
        self.enemies.draw(self.screen)
        self.hero.bullets.draw(self.screen)
        self.screen.blit(self.hero.image, self.hero.rect)
        self.walls.draw(self.screen)

    def run(self, game_type):
        # 单人模式类入口
        super(TankWarSingle, self).run(game_type)


