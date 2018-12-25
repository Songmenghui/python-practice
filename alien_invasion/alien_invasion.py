import sys


import pygame


from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
import game_functions as gf


def run_game():
    #初始化游戏创建一个屏幕对象
	pygame.init()
	'''创建显示窗口'''
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion made in NOBB")
	
	#创建play按钮
	play_button = Button(ai_settings,screen,"Play")
	#创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
    #创建一个飞船
	ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个alien的group
	aliens = Group()
	#创建aliens群
	gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        #每次循环都重新绘制屏幕
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
