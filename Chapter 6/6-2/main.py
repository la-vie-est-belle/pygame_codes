import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('pygame demo')

font = pygame.font.SysFont('consolas', 20)     # 1
font.set_bold(True)
font.set_italic(True)
font.set_underline(True)
font.set_strikethrough(True)
text = font.render('hello world', True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.center = (250, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)
    pygame.display.flip()
