import sys
import pygame

pygame.init()
surface1 = pygame.display.set_mode((800, 600))              # 1
pygame.display.set_caption('Surface Demo')

surface2 = pygame.image.load('pygame_logo.png')             # 2
surface2_rect = surface2.get_rect()
surface2_rect.center = (400, 300)

surface3 = pygame.image.load('python_logo.png')             # 3
surface3_rect = surface3.get_rect()
surface3_rect.topleft = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface1.fill((0, 255, 0), (0, 0, 400, 600))            # 4
    surface1.blit(surface2, surface2_rect)                  # 5

    surface2.blit(surface3, surface3_rect)                  # 6

    pygame.display.flip()