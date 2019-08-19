import pygame
import random


class Player:
    speed = 15
    def __init__(self, width, height,  x_pos, y_pos):
        self.width = width
        self.height = height
        self.pygame_object = pygame.Surface((width, height))
        self.pygame_object.fill((255, 255, 255))
        self.rect = self.pygame_object.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


class Ball:
    def __init__(self, x_pos, y_pos):
        self.speed = random.randint(10, 15)
        self.drop_direction = random.randint(-10, 10)
        self.pygame_object = pygame.Surface((20, 20))
        self.pygame_object.fill((255, 255, 255))
        self.rect = self.pygame_object.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
