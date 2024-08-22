import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_afk = pygame.image.load(r'python\\kissing_game\\assets\\player_afk.png').convert_alpha()
        self.player_caught = pygame.image.load(r'python\\kissing_game\\assets\\player_caught.png').convert_alpha()
        self.player_kiss = pygame.image.load(r'python\\kissing_game\\assets\\player_kiss.png').convert_alpha()
        self.image = self.player_afk
        self.rect = self.image.get_rect(midbottom=(400, 400))


    def player_input(self):
        keys = pygame.key.get_pressed()
        while keys[pygame.K_SPACE] == True:
            self.image = self.player_kiss
    
    def update(self):
        self.player_input()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Boykisser')
icon = pygame.image.load(r'python\\kissing_game\\icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

enemy = pygame.sprite.GroupSingle()
enemy.add(Enemy())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            __import__('sys').exit()
    
    bg = pygame.image.load(r'python\\kissing_game\\assets\\bg.png')
    window.blit(bg, (0, 0))
    
    player.draw(window)
    player.update()

    pygame.display.update()
    clock.tick(60)
