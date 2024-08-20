'''
бэк можно написать в пару строк в осн цикле

сцена 1:
    старт
сцена 2:
    если (нюша смотрит -> через рандом?) и (нажмали пробел или лкм):
        сцена 3:
            проиграли -> заново?
                -> да: сцена 2
                -> нет: сцена 1
'''

import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Boykisser')
fps = pygame.time.Clock()


def start_scene():
    pass


def game_scene():
    pass


def defeat_scene():
    pass

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            __import__('sys').exit()



    pygame.display.update()
    fps.tick(60)
