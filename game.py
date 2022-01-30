from game_logic.controller import Global
import pyglet
from pyglet.gl import *
import game_logic.variables as GLOB
from game_logic import game_objects
from game_logic import game_progress as save
global display_x, display_y
window = pyglet.window.Window(width=GLOB.display_width, height=GLOB.display_height)
window.set_vsync(False)
player_obj = game_objects.Player()
global bullet_list
bullet_list = []
enemy_list = []
for i in range(5):
    enemy_list.append(game_objects.Enemy())


def on_draw():
    window.clear()
    gl.glClearColor(0, 255, 0, 0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    player_obj.draw()
    for enemy in enemy_list:
        enemy.draw()
    for bullet in bullet_list:
        bullet.draw()
window.on_draw = on_draw
@window.event   
def on_key_press(symbol, modifiers):
    if symbol in GLOB.PLAYER_KEYS_GROUP:
        Global.Controller.Move.move(player_obj, 5, symbol)
    if symbol == GLOB.PLAYER_ATTACK:
        GLOB.fire = True
@window.event
def on_key_release(symbol, modifiers):
    if symbol in GLOB.PLAYER_KEYS_GROUP:
        Global.Controller.Move.stop(player_obj, 5, symbol) 
    if symbol == GLOB.PLAYER_ATTACK:
        GLOB.fire = False    


def update(dt, *args):
    # Global.Controller.Update.update_model(player_obj)
    player_obj.update()
    print(f"FPS is {pyglet.clock.get_fps()}")
    # Global.Controller.Update.update_model_by_other(bullet_list)
    for bullet in bullet_list:
        bullet.update()
    for enemy in enemy_list:
        enemy.update()    
    Global.TrashCollector.destroy(bullet_list)
    pass   
def shot(dt, *args):
    if GLOB.fire:
        bullet_list.append(game_objects.Bullet(player_obj))
def check_colisions(dt, *args):
    if enemy_list != [] and bullet_list != []:
        for bullet in bullet_list:
            for enemy in enemy_list: 
                try:
                    col = Global.Controller.Action.isCollision(bullet, enemy)
                except:
                    col = False
                if col:            
                    bullet_list.remove(bullet)
                    del bullet
                    enemy.hp -= 1
                    if enemy.hp == 0:
                        enemy_list.remove(enemy)
                        del enemy       
        
    
         
pyglet.clock.schedule_interval( update, 1/60 )
pyglet.clock.schedule_interval( shot, 1/10 )
pyglet.clock.schedule_interval( check_colisions, 1/30 )
pyglet.app.run()
#zrobić okno pauzy, mechanike okien, upgrade i trudność leveli

# def game(level_value = 1, reset_enemies = False):
#     enemy_a = []
#     enemies = 3
#     if reset_enemies:
#         for x in range(enemies):
#             enemy_obj = game_objects.Enemy(screen)
#             enemy_a.append(enemy_obj)

#     running = True
#     score = 0
#     while running:
#         screen.fill((100, 100, 0))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     player_obj.change = -0.8
#                 if event.key == pygame.K_RIGHT:
#                     player_obj.change = 0.8
#                 if event.key == pygame.K_SPACE:
#                    try:
#                        if bullet_obj.state == "ready":
#                            bullet_obj.state = "fire"
#                            bullet_obj.X = player_obj.X
#                    except:
#                        bullet_obj = game_objects.Bullet()
#                        if bullet_obj.state == "ready":
#                            bullet_obj.state = "fire"
#                            bullet_obj.X = player_obj.X
#                 if event.key == pygame.K_ESCAPE:
#                     running = False
#                     menu()
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     player_obj.change = 0
#         if player_obj.X <= 0:
#             player_obj.X = 0
#         elif player_obj.X >= 934:
#             player_obj.X = 934
#         player_obj.X += player_obj.change
#         for enemy in enemy_a:
#             if enemy.X <= 0:
#                 enemy.X_change = 0.3
#                 enemy.Y += enemy.Y_jump
#             elif enemy.X >= 934:
#                 enemy.X_change = -0.3
#                 enemy.Y += enemy.Y_jump
#             enemy.X += enemy.X_change
#             try:
#                 collision = collisions.isCollision(bullet_obj, enemy)
#             except:
#                 collision = False
#             if collision:
#                 enemy.Y = 100
#                 del bullet_obj

#             if enemy.hp == 0:
#                 del enemy_a[enemy_a.index(enemy)]
#                 del enemy
#                 progress.cash += 10
#                 score += 1
#             else:
#                 enemy.enemy(screen)
#         if enemy_a.__len__() == 0:
#             running = False
#             level()
#         try:
#             if bullet_obj.state == "fire":
#                 bullet_obj.Y -= bullet_obj.Y_change
#                 if bullet_obj.Y <= 0:
#                     bullet_obj.state = "ready"
#                     bullet_obj.Y = 480
#             bullet_obj.bullet(screen)
#         except:
#             0
#         wynik = f"wynik: {score}"
#         score_text = game_objects.GameFonts(22)

#         screen.blit(score_text.texture(wynik), (20, 570))
#         player_obj.player(screen)
#         pygame.display.update()


# def menu(pause = False):
#     strzałka_menu = game_objects.Pointer()
#     running = True
#     while running:
#         screen.fill((100, 100, 255))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     strzałka_menu.update_statement(True)
#                     key_not_lock = False
#                 if event.key == pygame.K_UP:
#                     strzałka_menu.update_statement(False)
#                 if event.key == pygame.K_RETURN and strzałka_menu.statement == 1:
#                     running = False
#                     level()
#                 if event.key == pygame.K_RETURN and strzałka_menu.statement == 2:
#                     running = False

#         for text in MENU_TEXT['texts']:
#             texture = game_objects.GameFonts(60)
#             x, y = MENU_TEXT['start_cords'][0], MENU_TEXT['start_cords'][1] * (MENU_TEXT['texts'].index(text) + 1)
#             screen.blit(texture.texture(text), (x, y))

#         strzałka_menu.render(screen)
#         pygame.display.update()

