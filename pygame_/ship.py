import pygame


class Ship():
    def __init__(self, screen, ai_settions):

        """初始化飞船并设置其位置"""
        self.screen = screen
        self.ai_settions = ai_settions

        # 加载飞船图像并获得其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.move_right = False
        self.move_left = False

        self.center = float(self.rect.centerx)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settions.ship_speed_factor

        elif self.move_left and self.rect.left > 0:
            self.center -= self.ai_settions.ship_speed_factor
        #
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
