import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('pygame demo')

font = pygame.font.SysFont('Arial', 32)
text = None
text_rect = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEMOTION:      # 1
            text = font.render('mouse motion', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            print(event.dict)

        elif event.type == pygame.MOUSEWHEEL:       # 2
            text = font.render('mouse wheel', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            print(event.dict)

        elif event.type == pygame.MOUSEBUTTONDOWN:  # 3
            if event.button == 1:
                text = font.render('left mouse button pressed', True, (0, 0, 0))
            elif event.button == 2:
                text = font.render('mid mouse button pressed', True, (0, 0, 0))
            elif event.button == 3:
                text = font.render('right mouse button pressed', True, (0, 0, 0))

            text_rect = text.get_rect()
            text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            print(event.dict)

        elif event.type == pygame.MOUSEBUTTONUP:    # 4
            if event.button == 1:
                text = font.render('left mouse button released', True, (0, 0, 0))
            elif event.button == 2:
                text = font.render('mid mouse button released', True, (0, 0, 0))
            elif event.button == 3:
                text = font.render('right mouse button released', True, (0, 0, 0))

            text_rect = text.get_rect()
            text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            print(event.dict)

    screen.fill((255, 255, 255))
    if text:
        screen.blit(text, text_rect)
    pygame.display.flip()