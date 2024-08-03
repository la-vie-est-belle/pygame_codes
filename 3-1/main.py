import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Dino Runner')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

land = pygame.image.load('land.png').convert_alpha()
land_rect = land.get_rect()
land_rect.y = 520                                   # 1

dino = pygame.image.load('dino_start.png').convert_alpha()
dino_rect = dino.get_rect()
dino_rect.topleft = (80, 450)                       # 2

flower = pygame.image.load('flower.png').convert_alpha()
flower_rect = flower.get_rect(topleft=(70, 10))     # 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(land, land_rect)
    screen.blit(dino, dino_rect)
    dino.blit(flower, flower_rect)

    pygame.display.flip()

