import sys
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame demo')

rect_area = pygame.Rect(0, 0, 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.arc(screen, (255, 0, 0), (10, 10, 100, 100), 0, math.pi)    # 1
    pygame.draw.arc(screen, (0, 0, 255), (10, 10, 100, 100), math.pi, math.pi*2)
    pygame.display.flip()
