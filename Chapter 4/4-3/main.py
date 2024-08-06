import sys
import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame demo')

rect_area = pygame.Rect(0, 0, 100, 100)
rect_area_copy1 = rect_area.copy()                      # 1
rect_area_copy1.topleft = (50, 50)
rect_area_copy2 = rect_area.copy()
rect_area_copy2.topleft = (10, 60)

rect_area = rect_area.move(10, 10)                      # 2
rect_area.scale_by_ip(0.5, 0.5)                         # 3

print(rect_area.contains(rect_area_copy1))              # 4
print(rect_area.colliderect(rect_area_copy1))           # 5
print(rect_area.collidelistall([rect_area_copy1, rect_area_copy2]))  # 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), rect_area)
    pygame.draw.rect(screen, (0, 0, 255), rect_area_copy1)
    pygame.draw.rect(screen, (255, 0, 0), rect_area_copy2)
    pygame.display.flip()
