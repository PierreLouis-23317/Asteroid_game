from turtle import position
import pygame
import sys
from pygame.math import Vector2

xscreen = 1280
yscreen = 800

pygame.init()
screen = pygame.display.set_mode((xscreen,yscreen)) #ici on met le arriere plan
pygame.display.set_caption("astéroïde")
clock = pygame.time.Clock()

asteroide_1 = pygame.draw.circle (screen, "red", asteroide pos, 40)
asteroide_2 = pygame.draw.circle (screen, "red", asteroide pos, 20)
asteroide_3 = pygame.draw.circle (screen, "red", asteroide pos, 10)


class GameObject :
    def __init__(self,position,velocity,sprite):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #tout les elements 
    #toutes les updates
    
    pygame.display.update() #update l'image
    clock.tick(60)

