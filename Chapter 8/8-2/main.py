import sys
import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super(Dino, self).__init__()
        self.image = pygame.image.load('dino_start.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(80, 450))

        self.speed = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= 1100 or self.rect.left <= 0:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)


class Bird(pygame.sprite.Sprite):               # 1
    def __init__(self, pos):
        super(Bird, self).__init__()
        self.image = pygame.image.load('bird.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= 300 or self.rect.bottom <= 0:
            self.speed = -self.speed


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((1100, 600))
    pygame.display.set_caption('Dino Runner')

    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    land = pygame.image.load('land.png').convert_alpha()
    land_rect = land.get_rect()
    land_rect.y = 520

    dino = Dino()

    bird_group = pygame.sprite.Group()          # 2
    for i in range(5):
        bird = Bird((80+i*220, i*10))
        bird_group.add(bird)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(land, land_rect)

        dino.draw(screen)
        dino.update()

        bird_group.draw(screen)                 # 3
        bird_group.update()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()