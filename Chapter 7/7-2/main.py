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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and event.mod == pygame.KMOD_LCTRL:  # 1
                text = font.render('CTRL+S', True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
                print(event.dict)

            if event.key == pygame.K_s and event.mod == pygame.KMOD_LCTRL + pygame.KMOD_LSHIFT:  # 2
                text = font.render('CTRL+Shift+S', True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
                print(event.dict)

    screen.fill((255, 255, 255))
    if text:
        screen.blit(text, text_rect)
    pygame.display.flip()