import sys
import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame demo')

rect_area = pygame.Rect(0, 0, 100, 100)
rect_area.topleft = (10, 10)                            # 1
print(rect_area.topleft)

rect_area.width = 200                                   # 2
rect_area.height = 300
print(rect_area.width)
print(rect_area.height)

rect_area.center = (int(screen.get_width()/2), int(screen.get_height()/2))  # 3
print(rect_area.center)
print(rect_area.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), rect_area)

    pygame.display.flip()