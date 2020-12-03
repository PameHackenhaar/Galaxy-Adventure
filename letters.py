import sys
import pygame
import pymunk
import random
import math
import os
from pymunk.vec2d import Vec2d
from pygame.color import *
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
image = pygame.image.load("assets_faces/HAPPY_FACE.png")
def to_pygame(p):
    return int(p.x), int(-p.y+600)
    
def add_ball(space):
    mass = 50
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia) 
    x = random.randint(120,380)
    body.position = x, 550 
    shape = pymunk.Circle(body, radius, (0,0)) 
    shape.elasticity = 0.95 
    space.add(body, shape) 
    return shape

def draw_ball(screen, ball):
    p = int(ball.body.position.x), 600-int(ball.body.position.y)
    pygame.draw.circle(screen, THECOLORS["black"], p, int(ball.radius), 2)

def add_static(space):
    body = pymunk.Body(pymunk.inf, pymunk.inf)
    body.position = (300,50)    
    l1 = pymunk.Segment(body, (-300, 0), (300.0, 0.0), 5.0) 
    l1.elasticity = 0.5        
    space.add(l1) 
    return l1

def draw_lines(screen, lines):
    body = lines.body
    pv1 = body.position + lines.a.rotated(math.degrees(body.angle)) 
    pv2 = body.position + lines.b.rotated(math.degrees(body.angle))
    p1 = to_pygame(pv1) 
    p2 = to_pygame(pv2)
    pygame.draw.lines(screen, THECOLORS["black"], False, [p1,p2])

def main():
    
    pymunk.init_pymunk()
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    ball = add_ball(space)
    print(ball.x) 
    running = True
    while running:
        screen.fill(THECOLORS["white"])
        screen.blit(image,[0,0])
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            
        lines = add_static(space)
        lines.eleasticity = 0.95
        draw_lines(screen, lines)
        draw_ball(screen, ball)
        dt = 1.0/60.0
        for x in range(1):
            space.step(dt)

        pygame.display.flip()
        clock.tick(50)
        
if __name__ == "__main__":
    main()