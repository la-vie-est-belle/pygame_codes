import sys
import pygame


def convert_coordinate(surface_width, surface_height, x, y):            # 1
    new_x = x + int(surface_width / 2)
    new_y = int(surface_height / 2) - y
    return new_x, new_y


pygame.init()
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Dino Runner')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

dino = pygame.image.load('dino_start.png').convert_alpha()
dino_rect = dino.get_rect()
dino_rect.topleft = convert_coordinate(screen.get_width(), screen.get_height(), 0, 0)   # 2
print(dino_rect.topleft)

flower = pygame.image.load('flower.png').convert_alpha()
flower_rect = flower.get_rect(topleft=convert_coordinate(dino.get_width(), dino.get_height(), 0, 0))    # 3
print(flower_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(dino, dino_rect)
    dino.blit(flower, flower_rect)

    pygame.display.flip()

