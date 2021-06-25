import pygame
import random


class Player:
    def __init__(self):
        self.playerImg = pygame.image.load('assets/space-invaders.png')
        self.X = 470.0
        self.Y = 480.0
        self.change = 0

    def player(self, screen):
        screen.blit(self.playerImg, (self.X, self.Y))


class Enemy:
    def __init__(self):
        self.enemyImg = pygame.image.load('assets/pixelated-alien.png')
        self.X = random.randrange(10, 980)
        self.Y = 100.0
        self.X_change = 0.3
        self.Y_change = 0
        self.Y_jump = 20

    def enemy(self, screen):
        screen.blit(self.enemyImg, (self.X, self.Y))


class Bullet:
    def __init__(self):
        self.bulletImg = pygame.image.load('assets/bullet.png')
        self.X = 0
        self.Y = 480
        self.X_change = 0
        self.Y_change = 1
        self.state = "ready"

    def bullet(self, screen):
        if self.state == "fire":
            screen.blit(self.bulletImg, (self.X, self.Y + 10))


class GameFonts:
    def __init__(self):
        self.font = pygame.font.Font('assets/fonts/mono.ttf', 60)

    def texture(self, text, color=0):
        color_font = color if color != 0 else (0, 0, 0)
        return self.font.render(text, False, color_font)


class Pointer:
    def __init__(self):
        self.image = pygame.image.load('assets/strzałka.png')
        self.X = 250
        self.Y = 150
        self.statement = 1

    def update_statement(self, state):
        if state:
            self.statement += 1
            if self.statement > 3:
                self.statement = 1
        else:
            self.statement -= 1
            if self.statement < 1:
                self.statement = 3

    def render(self, screen):
        screen.blit(self.image, (self.X, self.Y * self.statement))


