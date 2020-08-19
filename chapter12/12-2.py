import sys
import pygame


class Dog:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('dog.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.bg_color = self.image.get_at((0, 0)) # 以坐标（0，0）的颜色作为该元素的背景颜色

    def blitme(self):
        self.screen.blit(self.image, self.rect)

# 创建一个背景为蓝色的pygame窗口
def display_bg():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Display a blue window")
	little_dog = Dog(screen)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(little_dog.bg_color)
		little_dog.blitme()
		pygame.display.flip()


display_bg()