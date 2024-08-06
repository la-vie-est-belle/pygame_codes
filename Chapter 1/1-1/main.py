import sys
import pygame

pygame.init()                                       # 1
screen = pygame.display.set_mode((1100, 600))       # 2
pygame.display.set_caption('Dino Runner')           # 3

icon = pygame.image.load('icon.png')                # 4
pygame.display.set_icon(icon)

dino = pygame.image.load('dino_start.png')          # 5
dino_rect = dino.get_rect()
dino_rect.topleft = (80, 300)

while True:                                         # 6
    for event in pygame.event.get():                # 7
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))                    # 8
    screen.blit(dino, dino_rect)                    # 9
    pygame.display.flip()                           # 10
    # pygame.display.update((0, 0, 350, 350))

