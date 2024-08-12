import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('pygame demo')

font = pygame.font.SysFont('Arial', 32)             # 1
text = None
text_rect = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:          # 2
            if event.key == pygame.K_s:
                text = font.render('Key S pressed', True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
                print(event.dict)

        elif event.type == pygame.KEYUP:            # 3
            if event.key == pygame.K_s:
                text = font.render('Key S released', True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
                print(event.dict)

    screen.fill((255, 255, 255))
    if text:
        screen.blit(text, text_rect)
    pygame.display.flip()