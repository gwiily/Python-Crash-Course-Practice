import sys
import pygame


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.bg_color = self.image.get_at((0, 0)) # 以坐标（0，0）的颜色作为该元素的背景颜色
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down =False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
        	self.rect.centerx += 4
        if self.moving_left and self.rect.left > 0:
        	self.rect.centerx -= 4
        if self.moving_up and self.rect.top > 0:
        	self.rect.centery -= 4
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        	self.rect.centery += 4
            

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False


def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("A Rocket Game")
	my_rocket = Rocket(screen)
	while True:
		check_events(my_rocket)
		my_rocket.update()
		screen.fill(my_rocket.bg_color)
		my_rocket.blitme()
		pygame.display.flip()


run_game()