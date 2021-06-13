import pygame
import pygame.freetype

from game_logic import game_objects, collisions
clock = pygame.time.Clock()
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((1000, 600))
enemy_a = []
for x in range(5):
    enemy_obj = game_objects.Enemy()
    enemy_a.append(enemy_obj)
player_obj = game_objects.Player()
bullet_obj = game_objects.Bullet()
collisions = collisions.CollisionCalculate()


def game():
    running = True
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
                    if bullet_obj.state == "ready":
                        bullet_obj.state = "fire"
                        bullet_obj.X = player_obj.X
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
            collision = collisions.isCollision(bullet_obj, enemy)
            if collision:
                enemy.Y = 100
            enemy.enemy(screen)
        if bullet_obj.state == "fire":
            bullet_obj.Y -= bullet_obj.Y_change
            if bullet_obj.Y <= 0:
                bullet_obj.state = "ready"
                bullet_obj.Y = 480

        bullet_obj.bullet(screen)
        player_obj.player(screen)
        pygame.display.update()


def menu():
    running = True
    statement = 1
    while running:
        screen.fill((100, 100, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    statement += 1
                    key_not_lock = False
                    print(statement)
                if event.key == pygame.K_UP:
                    statement -= 1
                    print(statement)


        start = pygame.draw.rect(screen, (255, 0, 255), (200,statement * 100, 120, 100))  # okno, kolor, X,Y, szerokosc, wysokosc
        pygame.display.update()


menu()
