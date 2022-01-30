from contextlib import nullcontext
import pyglet
import random
import game_logic.variables as V
class Player:
    def __init__(self):
        self.playerImg = pyglet.resource.image('assets/statek.png')
        
        self.X = 100.0
        self.Y = 100.0
        self.changeY = 0.0
        self.changeX = 0.0


    def draw(self):
        return self.playerImg.blit(self.X, self.Y)
    def update(self):
        self.X += self.changeX
        self.Y += self.changeY
        if self.X < 0:
            self.X = 0
        if self.X > V.display_width - 40:
            self.X = V.display_width - 40
        if self.Y < 0:
            self.Y = 0
        if self.Y > V.display_height - 60:
            self.Y = V.display_height - 60    


class Enemy:
    def __init__(self):
        self.enemyImg = pyglet.resource.image('assets/ufo.png')
        self.X = random.randrange(10, 900)
        self.Y = V.display_height - 100
        self.changeX = 4
        self.changeY = 0
        self.Y_jump = 20
        self.hp = 10

    def draw(self):
        return self.enemyImg.blit(self.X, self.Y)
    def update(self):
        self.X += self.changeX
        self.Y += self.changeY
        if self.X < 0:
            self.changeX = 4
        if self.X > V.display_width - 100:
            self.changeX = -4
    def __del__(self):
        return True




class Bullet:
    def __init__(self, data=None):
        self.bulletImg = pyglet.resource.image('assets/bullet.png')
        self.X = data.X + 2
        self.Y = data.Y + 40
        self.changeX = 0
        self.changeY = 8.75

    def draw(self):
        return self.bulletImg.blit(self.X, self.Y)
    def __del__(self):
        return True
    def update(self):
        self.X += self.changeX
        self.Y += self.changeY


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


