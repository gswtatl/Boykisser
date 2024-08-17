import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Boykisser')
clock = pygame.time.Clock()


def draw(window):
    # Background
    pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            __import__('sys').exit()

    draw(window)

    pygame.display.update()
    clock.tick(60)
