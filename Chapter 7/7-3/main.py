import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('pygame demo')

font = pygame.font.SysFont('Arial', 32)             # 1
text = None
text_rect = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()                     # 1
    if keys[pygame.K_s]:                                # 2
        text = font.render('S', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)

    elif keys[pygame.K_a] and keys[pygame.K_LCTRL]:     # 3
        text = font.render('CTRL+A', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)

    screen.fill((255, 255, 255))
    if text:
        screen.blit(text, text_rect)
    pygame.display.flip()