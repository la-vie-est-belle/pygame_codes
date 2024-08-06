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
    pygame.draw.circle(screen, (0, 0, 255), (200, 200), 50)     # 1
    pygame.draw.ellipse(screen, (0, 255, 0), (300, 300, 50, 100), width=2)
    pygame.display.flip()
