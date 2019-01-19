import pygame
import os
# DEBUT LEVEL 1 : MonsterInvasion

def hero (ecran,x,y):
	fenetre.blit (hero_img(hero_x,hero_y))

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

finir = False

	# Evenements en fonction des touches

while not finir:
	for event in pygame.event.get():
	   if event.type == pygame.QUIT:
	       finir = True

	   if event.type == pygame.KEYDOWN:

        #Quand on appuie sur la touche :
	       if event.type == pygame.K_RIGHT or event.type == pygame.K_d:
	           hero_vitesse_x = 5

	       if event.type == pygame.K_LEFT or event.type == pygame.K_q:
	           hero_vitesse_x = -5

	       if event.type == pygame.K_UP or event.type == pygame.K_SPACE or event.type == pygame.K_z:
	           hero_vitesse_y = -5

<<<<<<< HEAD
	   if event.type == pygame.KEYUP:

        #Quand on lache sur la touche :

	       if event.type == pygame.K_RIGHT or event.type == pygame.K_d:
	           hero_vitesse_x = 0
=======
			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_RIGHT or event.type == pygame.K_d: # Deplacement Droite
					hero_vitesse_x = 0

				if event.type == pygame.K_LEFT or event.type == pygame.K_q: # Deplacement Gauche
					hero_vitesse_x = 0

				if event.type == pygame.K_UP or event.type == pygame.K_SPACE or event.type == pygame.K_z: # Deplacement saut
					hero_vitesse_y = 5
>>>>>>> 15192f64fb90da65983e9807a0c106683074cafd

	       if event.type == pygame.K_LEFT or event.type == pygame.K_q:
	           hero_vitesse_x = 0

	       if event.type == pygame.K_UP or event.type == pygame.K_SPACE or event.type == pygame.K_z:
	           hero_vitesse_y = 5

    hero_x = hero_x + hero_vitesse_x # !! Probleme d'indentation !!#
    hero_y = hero_y + hero_vitesse_y

	ecran.fill(background) # Effacement de l'ecran
	clock.tick(60) # Images pas seconde

pygame.quit()

