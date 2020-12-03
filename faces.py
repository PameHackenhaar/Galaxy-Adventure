import pygame
import os
import sys
from random import randint
from pygame.locals import *
EXEC_DIR = os.path.dirname(__file__)


class Face(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if sys.platform == "darwin":
            face_path = "assets_faces"
        else:
            face_path = os.path.join(EXEC_DIR, "assets_faces")
        if self.type == "happy":
            self.image = pygame.image.load(os.path.join(face_path,"HAPPY_FACE.png"))
        elif self.type == "sad":
            self.image = pygame.image.load(os.path.join(face_path, "SAD_FACE.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = [250, 350]
        self.lifespan = 15 
    
    def update(self):
        self.lifespan -= 1
        if self.type == "happy":
            x, y = (randint(1,500), randint(1,500))
        else:
            x, y = [250, 350]
        self.rect.topleft = [x, y]

    def reset(self):
        self.lifespan = 25