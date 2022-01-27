import pyglet
import random

class Player:
    def __init__(self):
        self.playerImg = pyglet.resource.image('assets/statek.png')
        
        self.X = 100.0
        self.Y = 100.0
        self.changeY = 0.0
        self.changeX = 0.0


    def draw(self):
        return self.playerImg.blit(self.X, self.Y)


class Enemy:
    def __init__(self, screen):
        self.enemyImg = pyglet.resource.image('assets/ufo.png')
        self.X = random.randrange(10, 900)
        self.Y = 100.0
        self.X_change = 0.2
        self.Y_change = 0
        self.Y_jump = 20
        self.hp = 10

    def enemy(self, screen):
        screen.blit(self.enemyImg, (self.X, self.Y))
        # pygame.draw.rect(screen, (255, 0, 0), (self.X, self.Y - 15, 70, 5))
        # pygame.draw.rect(screen, (0, 255, 0), (self.X, self.Y - 15, 7 * self.hp, 5))




class Bullet:
    def __init__(self):
        self.bulletImg = pyglet.resource.image('assets/bullet.png')
        self.X = 0
        self.Y = 480
        self.X_change = 0
        self.Y_change = 0.75
        self.state = "ready"

    def bullet(self, screen):
        if self.state == "fire":
            screen.blit(self.bulletImg, (self.X, self.Y + 10))


# class GameFonts:
#     def __init__(self, font_size):
#         self.font = pygame.font.Font('assets/fonts/mono.ttf', font_size)

#     def texture(self, text, color=0):
#         color_font = color if color != 0 else (0, 0, 0)
#         return self.font.render(text, False, color_font)


class Pointer:
    def __init__(self):
        # self.image = pygame.image.load('assets/strzałka.png').convert_alpha()
        self.X = 250
        self.Y = 150
        self.statement = 1

    def update_statement(self, state):
        if state:
            self.statement += 1
            if self.statement > 2:
                self.statement = 1
        else:
            self.statement -= 1
            if self.statement < 1:
                self.statement = 2
    def update_statementV2(self, state, show, array):
        if show.__len__() <= 1:
            return show
        array_len = array.__len__()
        if state:
            if array_len == state:
                return show
            self.statement += 1
            if self.statement > 2:
                self.statement = 1
        else:
            if array_len == state:
                return show
            self.statement -= 1
            if self.statement < 1:
                self.statement = 2

    def render(self, screen):
        screen.blit(self.image, (self.X, self.Y * self.statement))


