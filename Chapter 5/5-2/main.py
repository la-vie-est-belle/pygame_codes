import sys
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
    pygame.draw.rect(screen, (255, 0, 0), rect_area)     # 1
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 100, 100), width=0, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 255), (200, 200, 100, 100), width=1, border_radius=20)
    pygame.display.flip()
