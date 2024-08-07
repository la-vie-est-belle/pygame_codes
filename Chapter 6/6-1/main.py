import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame demo')

font1 = pygame.font.SysFont('consolas', 20, True, True)     # 1
text1 = font1.render('hello world', True, (255, 0, 0), (0, 0, 0))
text1_rect = text1.get_rect()
text1_rect.center = (250, 100)

font2 = pygame.font.Font('pixel.ttf', 32)                   # 2
text2 = font2.render('hello pygame', True, (0, 255, 0))
text2_rect = text2.get_rect()
text2_rect.center = (250, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(text1, text1_rect)                          # 3
    screen.blit(text2, text2_rect)
    pygame.display.flip()
