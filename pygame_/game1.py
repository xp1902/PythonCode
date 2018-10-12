import sys
import pygame
from settings import Settings
from ship import Ship
import game_fuctions as gf

from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        # 删除消失的子弹
        gf.update_bullets(ai_settings, screen, ship, bullets)

        gf.update_aliens(ai_settings, ship, aliens)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
