import pygame
import os
from pygame.locals import *
# DEBUT LEVEL 1 : MonsterInvasion

def hero (x,y,image):
	ecran.blit (image,(x,y))

def ennemie(x,y,image):
    ecran.blit(image,(x,y))

def background(x,y,image):
    ecran.blit(image,(x,y))

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERT = (0, 255 , 0)
MARRON = (70, 46, 1)


pygame.init() # COMMENCEMENT DU JEU

# Gestion fenetre
fenetre_longeur = 1920 # Largeur fenetre
fenetre_largeur = 1080 # Hauteur Fentre

ecran = pygame.display.set_mode((fenetre_longeur, fenetre_largeur), RESIZABLE) # initialisation de la fenetre
pygame.display.set_caption("MonsterInvasion") # Nom de la fentre

# Gestion images
hero_img = pygame.image.load ("images/Hero.png")
fond_ecran = pygame.image.load ("images/FondGame.png")
ennemie_img = pygame.image.load("images/Ennemie.png")


# Resolution des personnages

largeur_hero = 200 # Resolution du hero (image largeur)
longeur_hero = 150 # Resolution du hero (image longueur)

largeur_ennemie = 150 # Resolution Ennemie (image largeur)
longeur_ennemie = 100 # Resolution Ennemie (image longueur)


#Coords de la platerforme du niveau 1
plateforme_lvl1_x = 0
plateforme_lvl1_y = fenetre_largeur - (fenetre_largeur/4) # La plateforme prend un quart de l'écran

# Coords du hero
hero_x = fenetre_longeur/2 - longeur_hero/2 # Le Hero est centré
hero_y = plateforme_lvl1_y - largeur_hero # Le Hero spawn sur la plateforme

# Coords de l'imge de fond
background_x = 0
background_y = 0


# Vitesse Hero
hero_vitesse_x = 0
hero_vitesse_y = 0

# Acceleration Hero
hero_acceleration_x = 0
hero_acceleration_y = 0

# Coord Ennemie
ennemie_x = 0
ennemie_y = plateforme_lvl1_y - largeur_ennemie

# Vitesse Ennemie
ennemie_vitesse_x = 0
ennemie_vitesse_y = 0

#Variable pour l'acceleration
a = 0

clock = pygame.time.Clock()

finir = False

	# Evenements en fonction des touches

while not finir:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finir = True
        if event.type == pygame.KEYDOWN:

# Quand on appuie sur la touche :
            if event.key == pygame.K_LEFT: # Gauche

                hero_acceleration_x = -2
                a = 1
                hero_img = pygame.image.load ("images/Hero_gauche.png")

            if event.key == pygame.K_RIGHT: # Droite

                hero_acceleration_x = 2
                a = 2
                hero_img = pygame.image.load ("images/Hero.png")

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # Saut

                if hero_y + largeur_hero == plateforme_lvl1_y : # barre espace uniquement possible s le personnage est sur la platerforme
                    hero_vitesse_y = (-3*fenetre_largeur/100)

            if event.key == pygame.K_DOWN: # Descendre

                hero_vitesse_y = (3*fenetre_largeur/100)

        if event.type == pygame.KEYUP:
# Quand on lache la touche :
            if event.key == pygame.K_LEFT:

                hero_vitesse_x = 0
                hero_acceleration_x = 0
                a = 0

            if event.key == pygame.K_RIGHT:

                hero_vitesse_x = 0
                hero_acceleration_x = 0
                a = 0

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP :

                hero_vitesse_y = 0

            if event.key == pygame.K_DOWN:

                hero_vitesse_y = 0

    hero_x = hero_x + hero_vitesse_x
    hero_y = hero_y + hero_vitesse_y

    if hero_acceleration_y != 0:
        hero_vitesse_y = hero_vitesse_y + hero_acceleration_y

    if hero_acceleration_x != 0:
        hero_vitesse_x = hero_vitesse_x + hero_acceleration_x

    if a == 2: # acceleration a droite
        if hero_vitesse_x < 4:
            hero_acceleration_x = hero_acceleration_x + 1.5
    if a == 1: # acceleration a gauche
        if hero_vitesse_x > 4:
            hero_acceleration_x = hero_acceleration_x - 1.5






# Colisions avec la plateforme
    if hero_y + largeur_hero > plateforme_lvl1_y:
        hero_y = plateforme_lvl1_y - largeur_hero



# Ennemie qui suit Hero / Automatique

    if ennemie_x<hero_x:
        ennemie_vitesse_x = (1*fenetre_longeur/100)
        ennemie_x = ennemie_x + ennemie_vitesse_x
        ennemie_img = pygame.image.load("images/Ennemie.png")
    if ennemie_x>hero_x:
        ennemie_vitesse_x = (-1*fenetre_longeur/100)
        ennemie_x = ennemie_x + ennemie_vitesse_x
        ennemie_img = pygame.image.load("images/Ennemie_gauche.png")

    ecran.fill(0)

    # DEBUT DE L'AFFICHAGE

    background(background_x, background_y, fond_ecran)
    hero(hero_x,hero_y,hero_img)
    ennemie(ennemie_x, ennemie_y, ennemie_img)

    #placement de la plateforme + fine couche
    pygame.draw.rect(ecran,MARRON,[plateforme_lvl1_x,plateforme_lvl1_y,fenetre_longeur,fenetre_largeur]) # plateforme du niveau 1
    pygame.draw.rect(ecran,VERT,[plateforme_lvl1_x,plateforme_lvl1_y,fenetre_longeur,7.5])


    pygame.display.flip()
    clock.tick(60)



pygame.quit() # FIN

