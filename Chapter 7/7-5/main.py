import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('pygame demo')

font = pygame.font.SysFont('Arial', 32)
text = None
text_rect = None

CUSTOM_EVENT1 = pygame.USEREVENT            # 1
CUSTOM_EVENT2 = pygame.USEREVENT + 1

event1 = pygame.event.Event(CUSTOM_EVENT1, attr1='value1', attr2='value2')
pygame.event.post(event1)                   # 2

pygame.time.set_timer(CUSTOM_EVENT2, 1000)  # 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == CUSTOM_EVENT1:   # 4
            text = font.render('CUSTOM EVENT 1', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            print(event.dict)

        elif event.type == CUSTOM_EVENT2:   # 4
            text = font.render('CUSTOM EVENT 2', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            print(event.dict)

    screen.fill((255, 255, 255))
    if text:
        screen.blit(text, text_rect)
    pygame.display.flip()
