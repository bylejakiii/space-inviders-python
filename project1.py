import pygame
import pygame.freetype

from game_logic import game_objects, collisions
from game_logic import game_progress as save
MENU_TEXT = {'texts': ["START", "WYJSCIE"], 'start_cords': [400, 150]}
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
pygame.init()
display_x = 1000
display_y = 600
screen = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption("Space Inviders - WSB")
enemy_a = []
enemies = 3
for x in range(enemies):
    enemy_obj = game_objects.Enemy(screen)
    enemy_a.append(enemy_obj)
player_obj = game_objects.Player()
collisions = collisions.CollisionCalculate()
progress = save.Progress()


def game():
    running = True
    score = 0
    while running:
        screen.fill((100, 100, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_obj.change = -0.8
                if event.key == pygame.K_RIGHT:
                    player_obj.change = 0.8
                if event.key == pygame.K_SPACE:
                   try:
                       if bullet_obj.state == "ready":
                           bullet_obj.state = "fire"
                           bullet_obj.X = player_obj.X
                   except:
                       bullet_obj = game_objects.Bullet()
                       if bullet_obj.state == "ready":
                           bullet_obj.state = "fire"
                           bullet_obj.X = player_obj.X
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_obj.change = 0
        if player_obj.X <= 0:
            player_obj.X = 0
        elif player_obj.X >= 934:
            player_obj.X = 934
        player_obj.X += player_obj.change
        for enemy in enemy_a:
            if enemy.X <= 0:
                enemy.X_change = 0.3
                enemy.Y += enemy.Y_jump
            elif enemy.X >= 934:
                enemy.X_change = -0.3
                enemy.Y += enemy.Y_jump
            enemy.X += enemy.X_change
            try:
                collision = collisions.isCollision(bullet_obj, enemy)
            except:
                collision = False
            if collision:
                enemy.Y = 100
                del bullet_obj

            if enemy.hp == 0:
                del enemy_a[enemy_a.index(enemy)]
                del enemy
                score += 1
            else:
                enemy.enemy(screen)
        try:
            if bullet_obj.state == "fire":
                bullet_obj.Y -= bullet_obj.Y_change
                if bullet_obj.Y <= 0:
                    bullet_obj.state = "ready"
                    bullet_obj.Y = 480
            bullet_obj.bullet(screen)
        except:
            0
        wynik = f"wynik: {score}"
        score_text = game_objects.GameFonts(22)

        screen.blit(score_text.texture(wynik), (20, 570))
        player_obj.player(screen)
        pygame.display.update()


def menu():
    strzałka = game_objects.Pointer()
    running = True
    while running:
        screen.fill((100, 100, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    strzałka.update_statement(True)
                    key_not_lock = False
                if event.key == pygame.K_UP:
                    strzałka.update_statement(False)
                if event.key == pygame.K_RETURN and strzałka.statement == 1:
                    running = False
                    game()
                if event.key == pygame.K_RETURN and strzałka.statement == 2:
                    running = False

        for text in MENU_TEXT['texts']:
            texture = game_objects.GameFonts(60)
            x, y = MENU_TEXT['start_cords'][0], MENU_TEXT['start_cords'][1] * (MENU_TEXT['texts'].index(text) + 1)
            screen.blit(texture.texture(text), (x, y))

        strzałka.render(screen)
        pygame.display.update()


menu()
progress.save_game()
