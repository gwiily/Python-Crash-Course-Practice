import sys
import pygame


# 创建一个背景为蓝色的pygame窗口
def display_blue():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Display a blue window")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill((0, 0, 255))
		pygame.display.flip()


display_blue()