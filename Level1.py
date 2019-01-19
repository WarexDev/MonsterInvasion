import pygame
import os
# DEBUT LEVEL 1 : MonsterInvasion

def hero (ecran,x,y):
	fenetre.blit (hero_img(hero_x,hero_y))

def ennemie(ecran,xy):
    fenetre.blit(ennemie_img(ennemie_x, ennemie_y))

pygame.init()

# Gestion fenetre
fenetre_longeur = 1280 # Largeur fenetre
fenetre_largeur = 720 # Hauteur Fentre

ecran = pygame.display.set_mode((fenetre_longeur, fenetre_largeur)) # initialisation de la fenetre
pygame.display.set_caption("MonsterInvasion") # Nom de la fentre

# Gestion images
hero_img = pygame.image.load (os.path.join("Hero.png"))
background = pygame.image.load (os.path.join("FondGame.jpg")) # Pas encore dans le fichier


# Coord Hero
hero_x = fenetre_longeur/2 + largeur_hero
hero_y = fenetre_largeur/2 - longeur_hero
# Vitesse Hero
hero_vitesse_x = 0
hero_vitesse_y = 0


# Coord Ennemie
ennemie_x = 0
ennemie_y = 0
# Vitesse Ennemie
ennemie_vitesse_x = 0
ennemie_vitesse_y = 0

finir = False

	# Evenements en fonction des touches

while not finir:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finir = True
        if event.type == pygame.KEYDOWN:

# Quand on appuie sur la touche :
            if event.key == pygame.K_LEFT:
                hero_vitesse_x = -5
            if event.key == pygame.K_RIGHT:
                hero_vitesse_x = 5
            if event.key == pygame.K_UP:
                hero_vitesse_y = -5

        if event.type == pygame.KEYUP:
# Quand on lache la touche :
            if event.key == pygame.K_LEFT:
                x_vitesse = 0
            if event.key == pygame.K_RIGHT:
                x_vitesse = 0
            if event.key == pygame.K_UP:
                y_vitesse = 5

    hero_x = hero_x + hero_vitesse_x
    hero_y = hero_y + hero_vitesse_y


# Ennemie qui suit Hero / Automatique

    if ennemie_x<hero_x:
        ennemie_vitesse_x = 4
        hero_x = hero_x + hero_vitesse_x
    if ennemie_x<hero_x:
        hero_vitesse_x = -4
        hero_x = hero_x + hero_vitesse_x



pygame.quit()

