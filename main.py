import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.player_afk = pygame.image.load('assets\\player_afk.png').convert_alpha()
        self.player_caught = pygame.image.load('assets\\player_caught.png').convert_alpha()
        self.player_kiss = pygame.image.load('assets\\player_kiss.png').convert_alpha()

        self.image = self.player_afk
        self.rect = self.image.get_rect(midbottom=(450, 400))
        self.enemy = enemy

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.enemy.image == self.enemy.frames[2]:
                self.image = self.player_caught
            else:
                self.image = self.player_kiss
        else:
            self.image = self.player_afk

    def update(self):
        self.player_input()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        nyusha1 = pygame.image.load('assets\\nyusha1.png').convert_alpha()
        nyusha2 = pygame.image.load('assets\\nyusha2.png').convert_alpha()
        nyusha3 = pygame.image.load('assets\\nyusha3.png').convert_alpha()
        
        self.animation_index = 0
        self.frames = [nyusha1, nyusha2, nyusha3]
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(140, 400))
    
    def animation_state(self):
        self.animation_index += 0.01
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()


def main():
    pygame.init()
    audio = pygame.mixer.Sound('assets\\audio.mp3')
    audio.play(loops=-1).set_volume(0.5)
    window = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Boykisser')
    icon = pygame.image.load('assets\\icon.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    # Groups
    enemy = Enemy()
    player = Player(enemy)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy)

    # Timer
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 300)

    game_active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                __import__('sys').exit()
            if event.type == enemy_timer:
                enemy.update()
            if (not game_active and event.type == pygame.KEYDOWN and
                event.key == pygame.K_SPACE):
                    game_active = True

        if game_active:
            bg = pygame.image.load('assets\\bg.png')
            window.blit(bg, (0, 0))
            all_sprites.update()
            all_sprites.draw(window)
        else:
            window.fill('#25205e')
            font1 = pygame.font.Font('assets\\font.ttf', 90)
            name = font1.render('Boykisser', True, '#82b4ff')
            window.blit(name, name.get_rect(center=(350, 200)))
            font2 = pygame.font.Font('assets\\font.ttf', 30)
            start = font2.render('press space to start', True, '#ffffff')
            window.blit(start, start.get_rect(center=(350, 350)))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
