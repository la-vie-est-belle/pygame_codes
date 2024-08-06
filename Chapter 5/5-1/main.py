import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame demo')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (50, 150), width=2)       # 1
    pygame.draw.line(screen, (255, 0, 0), (50, 150), (150, 150), width=2)
    pygame.draw.line(screen, (255, 0, 0), (150, 150), (100, 100), width=2)

    pygame.draw.lines(screen, (0, 255, 0), False, [(200, 200), (150, 250), (250, 250)], width=2)  # 2
    pygame.display.flip()
