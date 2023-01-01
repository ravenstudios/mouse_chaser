import pygame
from constants import *
import random

class Particle:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.width, self.height = BLOCK_SIZE, BLOCK_SIZE
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = (r, g, b)


    def update(self):
        pass


    def draw(self, surface):
        bs = BLOCK_SIZE
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


    def get_pos(self):
        return (self.x, self.y)


    def set_pos(self, pos):
        self.x, self.y = pos
