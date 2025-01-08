import pygame
import sys
import math
import random


pygame.init()

#dimension écran
ecran = pygame.display.set_mode((800,800)) #bug si pas carré
longueur  = ecran.get_width()  
hauteur = ecran.get_height() 


#ici on load les images
le_vaisseau   = pygame.image.load('le_dossier_a_images/vaisseau_1.png')
le_asteroide  = pygame.image.load('le_dossier_a_images/asteroide_1.png')
le_background = pygame.image.load('le_dossier_a_images/fond_du_jeu.png')
le_icon       = pygame.image.load('le_dossier_a_images/logo_ecam.png')
#ici on les compresse
vaisseau = pygame.transform.scale(le_vaisseau, (40,40))
background = pygame.transform.scale(le_background, (hauteur,longueur))
asteroide_grand = pygame.transform.scale(le_asteroide, (150,150))
asteroide_moyen = pygame.transform.scale(le_asteroide, (100,100))
asteroide_petit = pygame.transform.scale(le_asteroide, (50,50))
icon = pygame.transform.scale(le_asteroide, (32,32))




#ici ces tous les routeurs pour le jeu
pygame.display.set_caption('the game asteroid by PIERRE Louis')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


class Vaisseau:
    def __init__(self):
        self.image = vaisseau
        self.x, self.y = int(longueur/2), int(hauteur/2) 
        #self.x = longueur//2
        #self.y = hauteur//2
        self.longueur = self.image.get_width()
        self.hauteur = self.image.get_height()
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0
        self.rotation = pygame.transform.rotate(self.image,self.angle)
        self.imagerotation = self.rotation.get_rect(center = (self.x, self.y))
        self.imagerotation.center = (self.x, self.y)

        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.canon = (self.x + self.cos * self.longueur//2, self.y - self.sin * self.hauteur//2)

    def draw(self,ecran):#erreur vient d'ici
        #ecran.blit(self.image,[self.x,self.y,self.longueur,self.hauteur]) #je comprends pas prq celui ci marche pas
        #ecran.blit(self.rotation,[self.x,self.y,self.longueur,self.hauteur])
        #ecran.blit(self.rotation,(self.x - int(self.longueur / 2),self.y - int(self.hauteur / 2)))
        ecran.blit(self.rotation,self.imagerotation)
        #ecran.blit(self.rotation,(self.x-20,self.y-20))
        #ecran.blit(self.rotation, self.rotatedRect.topleft)

    def rotation_gauche(self):
        self.angle += 5
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.imagerotation = self.rotation.get_rect()
        self.imagerotation.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.canon = (self.x + self.cos * self.longueur//2, self.y - self.sin * self.hauteur//2)
    
    def rotation_droite(self):
        self.angle -= 5
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.imagerotation = self.rotation.get_rect()
        self.imagerotation.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.canon = (self.x + self.cos * self.longueur//2, self.y - self.sin * self.hauteur//2)

    def bandage(self): #car beug
        self.angle += 0
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.imagerotation = self.rotation.get_rect()
        self.imagerotation.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.canon = (self.x + self.cos * self.longueur//2, self.y - self.sin * self.hauteur//2)


    def avance(self):
        vitesse = 0.1
        self.velocity_x += self.cos * vitesse
        self.velocity_y -= self.sin * vitesse
        #self.x += self.cos * 6
        #self.y -= self.sin * 6
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.imagerotation = self.rotation.get_rect()
        self.imagerotation.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.canon = (self.x + self.cos * self.longueur // 2, self.y - self.sin * self.hauteur // 2)



    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        #pour changer de coté
        if self.x >= longueur:
            self.x -= longueur
        elif self.x <= 0:
            self.x += longueur
        elif self.y >= hauteur:
            self.y -= hauteur
        elif self.y <= 0:
            self.y += hauteur

class rayon_laser:
    def __init__(self):
        self.canon = vaisseau_object.canon
        self.x,self.y = self.canon
        self.longeur = 2
        self.hauteur = 2
        self.cos = vaisseau_object.cos
        self.sin = vaisseau_object.sin
        vitesse = 5
        self.velocity_x = self.cos*vitesse
        self.velocity_y = self.sin*vitesse
        self.compteur = 0
    
    def update(self):
        self.x += self.velocity_x
        self.y -= self.velocity_y
        self.compteur += 1
        if self.x >= longueur:
                self.x -= longueur
        elif self.x <= 0:
            self.x += longueur
        elif self.y >= hauteur:
            self.y -= hauteur
        elif self.y <= 0:
            self.y += hauteur

    def draw(self,ecran):
        pygame.draw.rect(ecran,(255, 255, 255), [self.x, self.y, self.longeur, self.hauteur])
    
    def fin_de_vie(self):
        if self.compteur == 100 :
            return True

class Asteroid:
    def __init__(self, taille = random.randint(1,3), x=0, y=0):
        self.taille = taille
        #self.image
        if self.taille == 3:
            self.image = asteroide_grand
        elif self.taille == 2:
            self.image = asteroide_moyen
        elif self.taille == 1 :
            self.image = asteroide_petit
        else:
            print("error")
        if x == 0: #on imagine que aucun asteroide ne sera detruit en 0
            x_ou_y = random.randint(1,2)
            if x_ou_y == 1: #spawn sur axe x
                self.x = 0
                self.y =random.randint(0,hauteur) 
            elif x_ou_y == 2: #spawn sur axe y
                self.x = random.randint(0,longueur)
                self.y = 0
            else:
                print("error")
        else :
            self.x = x
            self.y = y
        nombre_entier = random.randint(-5,5)#exclure la velocity = 0
        while nombre_entier == 0:
            nombre_entier = random.randint(-5, 5)
        self.velocity_x = nombre_entier
        nombre_entier = random.randint(-5,5)
        while nombre_entier == 0:
            nombre_entier = random.randint(-5, 5)
        self.velocity_y = nombre_entier
        self.longueur = self.image.get_width()
        self.hauteur  = self.image.get_height()

    def draw(self,ecran):
            ecran.blit(self.image,(self.x - self.image.get_width() //2 ,self.y - self.image.get_height() // 2)) #on centre l'image
        
    def update(self):
            self.x += self.velocity_x
            self.y += self.velocity_y
            if self.x >= longueur:
                self.x -= longueur
            elif self.x <= 0:
                self.x += longueur
            elif self.y >= hauteur:
                self.y -= hauteur
            elif self.y <= 0:
                self.y += hauteur
    
    def division(self,x,y):
        if self.taille == 3:
            for i in range(3):
                asteroide_object.append(Asteroid(2,x,y))
        if self.taille == 2:
            for i in range(3):
                asteroide_object.append(Asteroid(1,x,y))
            

#creation d'une police de texte
police = pygame.font.Font(None, 36)


def afficher():
    ecran.blit(background,(0,0))
    
    score_1 = police.render("Score : " + str(score), True, (255, 255, 255))
    ecran.blit(score_1, (10, 10))
    vaisseau_object.draw(ecran)
    for i in rayon_laser_object:
        i.draw(ecran)
    for i in asteroide_object:
        i.draw(ecran)

    pygame.display.update()
    #pygame.display.flip()




vaisseau_object = Vaisseau()
rayon_laser_object = []
nombre_de_rayon = 0
asteroide_object = []
#nombre_asteroide = random.randint(2, 5)
nombre_asteroide = 2
score = 0

for i in range(1,nombre_asteroide + 1):
    #asteroide_object.append(Asteroid(random.randint(1,3))) #petit bandage ici aussi
    asteroide_object.append(Asteroid(1))
while True:
    clock.tick(60)
    vaisseau_object.update()
    for i in rayon_laser_object:
        i.update()
        if i.fin_de_vie():
            rayon_laser_object.pop(rayon_laser_object.index(i))
            nombre_de_rayon -= 1
    
    for i in asteroide_object:
        i.update()
    
    #check la collision entre rayon laser et asteroide
    for a in asteroide_object:
        for r in rayon_laser_object:
            if a.x - (a.longueur/2) * (1/(math.sqrt(2))) <= r.x <= a.x + (a.longueur/2) * (1/(math.sqrt(2))):
                if a.y - (a.hauteur/2) * (1/(math.sqrt(2))) <= r.y <= a.y + (a.hauteur/2) * (1/(math.sqrt(2))):
                    rayon_laser_object.pop(rayon_laser_object.index(r))
                    nombre_de_rayon -= 1
                    score +=50
                    a.division(a.x,a.y)
                    asteroide_object.pop(asteroide_object.index(a))    
            elif a.x - (a.longueur/2) * (1/2) <= r.x <= a.x + (a.longueur/2) * (1/2):
                if a.y - (a.hauteur/2) * (math.sqrt(3)/(2)) <= r.y <= a.y + (a.hauteur/2) * (math.sqrt(3)/2):
                    rayon_laser_object.pop(rayon_laser_object.index(r))
                    nombre_de_rayon -= 1
                    score += 50
                    a.division(a.x,a.y)
                    asteroide_object.pop(asteroide_object.index(a))      
            elif a.x - (a.longueur/2) * (math.sqrt(3)/2) <= r.x <= a.x + (a.longueur/2) * (math.sqrt(3)/2):
                if a.y - (a.hauteur/2) * (1/(math.sqrt(2))) <= r.y <= a.y + (a.hauteur/2) * (1/2):
                    rayon_laser_object.pop(rayon_laser_object.index(r))
                    nombre_de_rayon -= 1
                    score += 50
                    a.division(a.x,a.y)
                    asteroide_object.pop(asteroide_object.index(a))
                    
    
    #check la collsision entre asteroide et le joueur
    #je vais faire la même chose que avec les rayon laser et asteroide sauf que les pixel seront fixé au vaisseau
    for a in asteroide_object:
        if a.x - (a.longueur/2) * (1/(math.sqrt(2))) <= vaisseau_object.x  <= a.x + (a.longueur/2) * (1/(math.sqrt(2))):
                if a.y - (a.hauteur/2) * (1/(math.sqrt(2))) <= vaisseau_object.y + vaisseau_object.hauteur*(1/3) <= a.y + (a.hauteur/2) * (1/(math.sqrt(2))):
                    print(score)
                    sys.exit() #fin de partie
                    #ici il s'agit de l'avant du vaisseau
        if a.x - (a.longueur/2) * (1/(math.sqrt(2))) <= vaisseau_object.x + vaisseau_object.longueur*(1/3)  <= a.x + (a.longueur/2) * (1/(math.sqrt(2))):
                if a.y - (a.hauteur/2) * (1/(math.sqrt(2))) <= vaisseau_object.y - vaisseau_object.hauteur*(1/3) <= a.y + (a.hauteur/2) * (1/(math.sqrt(2))):
                    print(score)
                    sys.exit()
                    #il s'agit de arriere droit
        if a.x - (a.longueur/2) * (1/(math.sqrt(2))) <= vaisseau_object.x - vaisseau_object.longueur*(1/3)  <= a.x + (a.longueur/2) * (1/(math.sqrt(2))):
                if a.y - (a.hauteur/2) * (1/(math.sqrt(2))) <= vaisseau_object.y - vaisseau_object.hauteur*(1/3) <= a.y + (a.hauteur/2) * (1/(math.sqrt(2))):
                    print(score)
                    sys.exit()
                    #il s'agit de l'arriere gauche
        

    if asteroide_object == []:
        nombre_asteroide += 1
        for i in range(1,nombre_asteroide + 1):
            asteroide_object.append(Asteroid(random.randint(1,3)))
        

    #les touches
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vaisseau_object.rotation_gauche()
    if keys[pygame.K_RIGHT]:
        vaisseau_object.rotation_droite()
    if keys[pygame.K_UP]:
        vaisseau_object.avance()
    else:
        vaisseau_object.bandage()
    

    #les events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: #tire
            if event.key == pygame.K_SPACE:
                if nombre_de_rayon < 3: #c'est la cadence 
                    rayon_laser_object.append(rayon_laser())
                    nombre_de_rayon += 1
                    if score > 0:
                        score -= 1
    
                
    
    afficher()
    
    


pygame.quit()