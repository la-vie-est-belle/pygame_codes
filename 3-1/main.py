import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Surface Demo')

pygame_logo = pygame.image.load('pygame_logo.png').convert_alpha()  # 1
pygame_logo_rect = pygame_logo.get_rect()
pygame_logo_rect.center = (400, 300)
print(pygame_logo.get_size())                                       # 2
print(pygame_logo.get_width())
print(pygame_logo.get_height())

python_logo = pygame.image.load('python_logo.png').convert_alpha()
python_logo_rect = python_logo.get_rect()
python_logo_rect.topleft = (0, 0)
print(python_logo.get_size())
print(python_logo.get_width())
print(python_logo.get_height())

python_logo2 = python_logo.copy()                                   # 3
python_logo_rect2 = python_logo.get_rect()
python_logo_rect2.topright = (600, 100)
print(python_logo2.get_size())
print(python_logo2.get_width())
print(python_logo2.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 255, 0), (0, 0, 400, 600))
    screen.blit(pygame_logo, pygame_logo_rect)

    pygame_logo.blits(((python_logo, python_logo_rect), (python_logo2, python_logo_rect2)))  # 4

    pygame.display.flip()