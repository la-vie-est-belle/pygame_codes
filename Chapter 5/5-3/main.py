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
    pygame.draw.polygon(screen, (255, 0, 0), [(30, 400), (60, 80), (400, 380)])     # 1
    pygame.draw.polygon(screen, (0, 255, 0), [(450, 10), (450, 450), (300, 200), (400, 30)], width=1)
    pygame.display.flip()
