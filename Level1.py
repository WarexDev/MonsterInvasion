import pygame
import os
# DEBUT LEVEL 1 : MonsterInvasion

def hero (x,y,image):
	ecran.blit (image,(x,y))

def ennemie(x,y,image):
    ecran.blit(image,(x,y))

def background(x,y,image):
    ecran.blit(image,(x,y))

# Couleurs
WHITE = (255, 255, 255)


pygame.init()

# Gestion fenetre
fenetre_longeur = 1280 # Largeur fenetre
fenetre_largeur = 720 # Hauteur Fentre

ecran = pygame.display.set_mode((fenetre_longeur, fenetre_largeur)) # initialisation de la fenetre
pygame.display.set_caption("MonsterInvasion") # Nom de la fentre

# Gestion images
hero_img = pygame.image.load ("images/Hero.png")
fond_ecran = pygame.image.load ("images/FondGame.jpg") # Pas encore dans le fichier
ennemie_img = pygame.image.load("images/Ennemie.png") # Pas encore déans le fichier


# Coord Hero

largeur_hero = 10
longeur_hero = 20

hero_x = fenetre_longeur/2 + largeur_hero
hero_y = fenetre_largeur/2 - longeur_hero

background_x = 0
background_y = 0

# Vitesse Hero
hero_vitesse_x = 0
hero_vitesse_y = 0

# Coord Ennemie
ennemie_x = 0
ennemie_y = 0

# Vitesse Ennemie
ennemie_vitesse_x = 0
ennemie_vitesse_y = 0

clock = pygame.time.Clock()

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
                hero_vitesse_x = 0
            if event.key == pygame.K_RIGHT:
                hero_vitesse_x = 0
            if event.key == pygame.K_UP:
                hero_vitesse_y = 0

    hero_x = hero_x + hero_vitesse_x
    hero_y = hero_y + hero_vitesse_y


# Ennemie qui suit Hero / Automatique

    if ennemie_x<hero_x:
        ennemie_vitesse_x = 2
        ennemie_x = ennemie_x + ennemie_vitesse_x
    if ennemie_x>hero_x:
        ennemie_vitesse_x = -2
        ennemie_x = ennemie_x + ennemie_vitesse_x

    ecran.fill(WHITE)
    background(0, 0, fond_ecran)
    hero(hero_x,hero_y,hero_img)
    ennemie(ennemie_x, ennemie_y, ennemie_img)

    pygame.display.flip()
    clock.tick(60)



pygame.quit()

