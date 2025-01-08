import pygame
import sys
import random
import math

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids Game")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)

# Classe du vaisseau spatial
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('le_dossier_a_images/vaisseau_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.angle = 0

    def rotate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        self.image = pygame.transform.rotate(pygame.image.load("spaceship.png"), self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rotate()

# Initialisation du vaisseau spatial
spaceship = Spaceship()

# Boucle principale du jeu
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour du vaisseau spatial
    spaceship.update()

    # Effacer l'écran
    screen.fill(black)

    # Afficher le vaisseau spatial
    screen.blit(spaceship.image, spaceship.rect)

    # Rafraîchir l'écran
    pygame.display.flip()

    # Contrôle de la vitesse
    clock.tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()
