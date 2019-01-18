import pygame
# DEBUT LEVEL 1 : MonsterInvasion

pygame.init()

# Gestion fenetre
fenetre_longeur = 800 # Largeur fenetre
fenetre_largeur = 500 # Hauteur Fentre

resolution = pygame.display.set_mode((fenetre_longeur, fenetre_largeur)) # initialisation de la fenetre
pygame.display.set_caption("MonsterInvasion") # Nom de la fentre
 
# Gestion Hero
longeur_hero = #Hauteur a definir
largeur_hero= #Largeur a definir

def hero (hero_x,hero_y,hero_img):
	fenetre.blit (hero_img (hero_x,hero_y))


def main:
	hero_x = fenetre_longeur/2 + largeur_hero
	hero_y = fenetre_largeur/2 - longeur_hero

	hero_vitesse_x =
	hero_vitesse_ y =

	hero_img = pygame.image.load () #Chemin d'acces du personnage a mettre

	finir = False

	# Evenements en fonction des touches

	while finir = False:
		for event in pygame.event.get():
			if event.type == pygame.quit:
				finir = True

			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_RIGHT or event.type == pygame.K_d:
					hero_vitesse_x = 5

				if event.type == pygame.K_LEFT or event.type == pygame.K_q:
					hero_vitesse_x = -5

				if event.type == pygame.K_UP or event.type == pygame.K_SPACE or event.type == pygame.K_z:
					hero_vitesse_y = -5	

			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_RIGHT or event.type == pygame.K_d: # Deplacement Droite
					hero_vitesse_x = 0

				if event.type == pygame.K_LEFT or event.type == pygame.K_q: # Deplacement Gauche
					hero_vitesse_x = 0

				if event.type == pygame.K_UP or event.type == pygame.K_SPACE or event.type == pygame.K_z: # Deplacement saut
					hero_vitesse_y = 5



	pygame.fill() # Image de fond

	pygame.display.update() # Images pas seconde

main()
pygame.quit()
quit()

