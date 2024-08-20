import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Boykisser')
fps = pygame.time.Clock()


def start_menu():
    window.fill('#f5f5dc')
    font = pygame.font.Font(r'python\kissing_game\assets\font.TTF', 80)
    game_name = font.render('Boykisser', True, '#002137')
    window.blit(game_name, game_name.get_rect(center=(350, 150)))
    button_text = font.render('пробел пж', True, 'white', '#1fcecb')
    window.blit(button_text, button_text.get_rect(center=(350, 350)))

def game_scene():
    bg = pygame.image.load(r'python\kissing_game\assets\bg.png')
    window.blit(bg, (0, 0))


run = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            __import__('sys').exit()
        if not run:
            start_menu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run = True
        else:
            game_scene()

    pygame.display.update()
    fps.tick(60)
