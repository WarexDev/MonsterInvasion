import pygame
import os
from pygame.locals import *
from math import *
import time
# DEBUT LEVEL 1 : MonsterInvasion

#Debut parametres Hero

def parametre_hero_1(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,BLUE)
    ecran.blit(text, [20, 10])

def parametre_hero_2(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,BLUE)
    ecran.blit(text, [100, 10])

def parametre_hero_3(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,BLUE)
    ecran.blit(text, [200, 10])

def parametre_hero_4(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,BLUE)
    ecran.blit(text, [400, 10])

def parametre_hero_5(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,BLUE)
    ecran.blit(text, [600, 10])


#Fin parametres Hero

#Debut parametres ennemi

def parametre_ennemi_1(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,RED)
    ecran.blit(text, [20, 90])

def parametre_ennemi_2(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,RED)
    ecran.blit(text, [200, 90])

def parametre_ennemi_3(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,RED)
    ecran.blit(text, [400, 90])

def parametre_ennemi_4(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,RED)
    ecran.blit(text, [800, 90])

def parametre_ennemi_5(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,RED)
    ecran.blit(text, [1000, 90])

def parametre_fond_ecran(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,WHITE)
    ecran.blit(text, [1500, 90])

def parametre_grenade_x(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,WHITE)
    ecran.blit(text, [850, 110])

def parametre_grenade_y(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,WHITE)
    ecran.blit(text, [700, 110])

def parametre_hero_vie(mot):
    font = pygame.font.Font(None, 30)
    text = font.render(mot,True,WHITE)
    ecran.blit(text, [1000,1000])

def game_over(mot):
    font = pygame.font.Font(None, 500)
    text = font.render(mot,True,RED)
    ecran.blit(text, [fenetre_longeur/3, fenetre_largeur/3])

def game_over_options (mot, mot2):
    font. pygame.font.Font(None, 30)
    text = font.render(mot,True,WHITE)
    text_2 = font.render(mot,True,WHITE)
    ecran.blit(text, [fenetre_longeur/3, fenetre_largeur/3 + 600])
    ecran.blit(text_2, [fenetre_longeur/3 + 600, fenetre_largeur/3 + 600])




# Fin affichage des parametres de l'ennemi

def hero (x,y,image):
	ecran.blit (image,(x,y))

def ennemi(x,y,image):
    ecran.blit(image,(x,y))

def background(x,y,image):
    ecran.blit(image,(x,y))

def grenade(x,y,image):
    ecran.blit(image,(x,y))

def balle(x,y,image):
    ecran.blit(image,(x,y))

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERT = (0, 255 , 0)
MARRON = (70, 46, 1)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


pygame.init() # COMMENCEMENT DU JEU

# Gestion fenetre
fenetre_longeur = 1920  # Largeur fenetre
fenetre_largeur = 1080 # Hauteur Fentre

ecran = pygame.display.set_mode((fenetre_longeur, fenetre_largeur), RESIZABLE) # initialisation de la fenetre
pygame.display.set_caption("MonsterInvasion") # Nom de la fentre

# Gestion images
hero_img = pygame.image.load ("images/Hero_test.png")
fond_ecran = pygame.image.load ("images/FondGame2.jpg")
img_grenade = pygame.image.load ("images/Grenade.png")

# Pour de Gauche a Droite
ennemi_img1= pygame.image.load("images/ennemi/frame-01.png")
ennemi_img2= pygame.image.load("images/ennemi/frame-02.png")
ennemi_img3= pygame.image.load("images/ennemi/frame-03.png")
ennemi_img4= pygame.image.load("images/ennemi/frame-04.png")
ennemi_img5= pygame.image.load("images/ennemi/frame-05.png")
ennemi_img6= pygame.image.load("images/ennemi/frame-06.png")
ennemi_img7= pygame.image.load("images/ennemi/frame-07.png")
ennemi_img8= pygame.image.load("images/ennemi/frame-08.png")
ennemi_img9= pygame.image.load("images/ennemi/frame-09.png")
ennemi_img10= pygame.image.load("images/ennemi/frame-10.png")
ennemi_img11= pygame.image.load("images/ennemi/frame-11.png")
ennemi_img12= pygame.image.load("images/ennemi/frame-12.png")
ennemi_img13= pygame.image.load("images/ennemi/frame-13.png")
ennemi_img14= pygame.image.load("images/ennemi/frame-14.png")
ennemi_img15= pygame.image.load("images/ennemi/frame-15.png")
ennemi_img16= pygame.image.load("images/ennemi/frame-16.png")

### Pour de Droite a gauche Gif
##ennemi_img1_reverse= pygame.image.load("images/ennemi/frame-17.png")
##ennemi_img2_reverse= pygame.image.load("images/ennemi/frame-18.png")
##ennemi_img3_reverse= pygame.image.load("images/ennemi/frame-19.png")
##ennemi_img4_reverse= pygame.image.load("images/ennemi/frame-20.png")
##ennemi_img5_reverse= pygame.image.load("images/ennemi/frame-21.png")
##ennemi_img6_reverse= pygame.image.load("images/ennemi/frame-22.png")
##ennemi_img7_reverse= pygame.image.load("images/ennemi/frame-23.png")
##ennemi_img8_reverse= pygame.image.load("images/ennemi/frame-24.png")
##ennemi_img9_reverse= pygame.image.load("images/ennemi/frame-25.png")
##ennemi_img10_reverse= pygame.image.load("images/ennemi/frame-26.png")
##ennemi_img11_reverse= pygame.image.load("images/ennemi/frame-27.png")
##ennemi_img12_reverse= pygame.image.load("images/ennemi/frame-28.png")
##ennemi_img13_reverse= pygame.image.load("images/ennemi/frame-29.png")
##ennemi_img14_reverse= pygame.image.load("images/ennemi/frame-30.png")
##ennemi_img15_reverse= pygame.image.load("images/ennemi/frame-31.png")
##ennemi_img16_reverse= pygame.image.load("images/ennemi/frame-32.png")

# Gestion image balle
img_balle = pygame.image.load ("images/balle_droite.png")


# Resolution des objets / persos

largeur_hero = 140 # Resolution du hero (image largeur)
longeur_hero = 140 # Resolution du hero (image longueur)

largeur_ennemi = 140 # Resolution ennemi (image largeur)
longeur_ennemi =  140 # Resolution ennemi (image longueur)

largeur_grenade = 20 # Resolution grenade (image largeur)
longeur_grenade = 20 # Resolution grenade (image longueur)

longeur_balle = 50
largeur_balle = 25

largeur_background = 1080
longeur_background = 7680


#Coords de la platerforme du niveau 1
plateforme_lvl1_x = 0
plateforme_lvl1_y = fenetre_largeur - (fenetre_largeur/8) # La plateforme prend un quart de l'écran

# Coords du hero
hero_x = fenetre_longeur/2 - longeur_hero/2 # Le Hero est centré
hero_y = plateforme_lvl1_y - largeur_hero # Le Hero spawn sur la plateforme
hero_direction = 0

# Coords de l'imge de fond
background_x = 0
background_y = 0

background_x2 = longeur_background
background_x3 = 2*longeur_background


# Vitesse Hero
hero_vitesse_x = 0
hero_vitesse_y = 0
max_vitesse_x_hero = 50

# Vie et degats Hero
hero_vie = 100
hero_damage = 50

# Acceleration Hero
hero_acceleration_x = 0
hero_acceleration_y = 0

# Coord ennemi
ennemi_x = 0
ennemi_y = plateforme_lvl1_y - largeur_ennemi

#Pour saut
y_acceleration = 0

# Vitesse ennemi
ennemi_vitesse_x = 0
ennemi_vitesse_y = 0

#Vie Ennemi
ennemi_vie = 100
ennemi_damage = 20

#Variable pour l'acceleration
a = 0

#Coords Grenade et vitesse / acceleration
grenade_x = hero_x + longeur_hero/2
grenade_y = hero_y + largeur_hero/2

grenade_vitesse_x = 0
grenade_vitesse_y = 0

grenade_acceleration_y = 0
g= 0

#Coords balle
balle_x = hero_x + longeur_hero/2 # Au centre du hero
balle_y = hero_y + largeur_hero/2 # Au centre du hero

# Vitesses balle
balle_vitesse_x = 0
balle_vitesse_y = 0


# Animation ennemie
defil=0

clock = pygame.time.Clock()

finir = False

	# Evenements en fonction des touches

while not finir:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finir = True

        # Quand on appuie sur la touche :

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_LEFT: # Gauche

                hero_direction = 1 # je sais que mon hero va vers la gauche
                a = 1
                hero_img = pygame.image.load ("images/Hero_test_gauche.png")

            if event.key == pygame.K_RIGHT: # Droite

                hero_direction = 2 # je sais que mon hero va vers la droite
                a = 2
                hero_img = pygame.image.load ("images/Hero_test.png")

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # Saut

                if hero_y + largeur_hero == plateforme_lvl1_y :
                    hero_acceleration_y = - 30

            if event.key == pygame.K_DOWN: # Descendre
                g=1

            if event.key == MOUSEBUTTONDOWN and event.button == 1 :
                if hero_direction == 1 :
                    balle_vitesse_x = -10
                    img_balle = pygame.image.load ("images/balle_gauche.png")
                if hero_direction == 2 :
                    balle_vitesse_x = 10
                if hero_direction == 0 :
                    balle_vitesse_y = -10
                    img_balle = pygame.image.load ("images/balle_haut.png")


        # Quand on lache la touche :

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:

                hero_vitesse_x = 0
                hero_acceleration_x = 0
                a = 0

            if event.key == pygame.K_RIGHT:

                hero_vitesse_x = 0
                hero_acceleration_x = 0
                a = 0

            if event.key == pygame.K_DOWN:

                hero_vitesse_y = 0


    hero_x = hero_x + hero_vitesse_x
    hero_y = hero_y + hero_vitesse_y
    grenade_x = grenade_x + grenade_vitesse_x
    grenade_y = grenade_y + grenade_acceleration_y
    balle_x = balle_x + balle_vitesse_x
    balle_y = balle_y + balle_vitesse_y
    background_x = background_x - hero_vitesse_x

    if ennemi_y + largeur_ennemi < plateforme_lvl1_y :
        ennemi_y = ennemi_y + 30

    # Saut du personnage

    if hero_y + largeur_hero < plateforme_lvl1_y :
        hero_acceleration_y = hero_acceleration_y + 10
    else :
        hero_vitesse_y = 0

    if hero_acceleration_y != 0:
        hero_vitesse_y = hero_vitesse_y + hero_acceleration_y
        hero_acceleration_y = 0

    # Acceleration du personnage et de l'ecran

        # Quand on active l'acceleartion

    if hero_acceleration_x != 0:
        hero_vitesse_x = hero_vitesse_x + hero_acceleration_x

        # Acceleration a droite

    if a == 2:
        if hero_vitesse_x < max_vitesse_x_hero :
            hero_acceleration_x = hero_acceleration_x + 2
        else :
            hero_acceleration_x = 0

        # Acceleration a gauche

    if a == 1:
        if hero_vitesse_x > -max_vitesse_x_hero :
            hero_acceleration_x = hero_acceleration_x - 2
        else :
            hero_acceleration_x = 0

    # Caractéristiques de la balle

    if balle_x == ennemi_x + longeur_ennemi or balle_x + longeur_balle == ennemi_x :
        ennemi_vie = ennemi_vie - hero_damage
        balle_x = hero_x + longeur_hero/2 # Revient a la pos Initiale
        balle_y = hero_y + largeur_hero/2 # Revient a la pos Initiale

    if balle_x + longeur_balle < 0 or balle_x > fenetre_longeur or balle_y + longeur_balle < 0 :
        balle_x = hero_x + longeur_hero/2
        balle_y = hero_y + largeur_hero/2



# Colisions Hero
    if hero_y + largeur_hero > plateforme_lvl1_y: # plateforme colisions
        hero_y = plateforme_lvl1_y - largeur_hero
    if background_x !=0 and hero_x < 100 :
        hero_x = 100
    if background_x > 0:
        background_x = 0
    if hero_x + longeur_hero > fenetre_longeur - 100 :
        hero_x = fenetre_longeur - 100 - longeur_hero



# Ennemi qui suit Hero / Degats de Ennemi

    if ennemi_x + largeur_ennemi <hero_x and ennemi_y + largeur_ennemi == plateforme_lvl1_y:
        ennemi_vitesse_x = 5
        ennemi_x = ennemi_x + ennemi_vitesse_x

    if ennemi_x > hero_x + largeur_hero and ennemi_y + largeur_ennemi == plateforme_lvl1_y:
        ennemi_vitesse_x = -5
        ennemi_x = ennemi_x + ennemi_vitesse_x

    if ennemi_x + largeur_ennemi == hero_x or ennemi_x == hero_x + largeur_ennemi :
        hero_vie = hero_vie - ennemi_damage


 # Game Over / Quit game
    if hero_vie <= 0 :
        finir = True

    ecran.fill(0)

    # DEBUT DE L'AFFICHAGE

    background(background_x, background_y, fond_ecran)
    background(background_x2 + background_x, background_y, fond_ecran)
    background(background_x3 + background_x, background_y, fond_ecran)

    # Affichage des parametres

    parametre_hero_1(str(hero_x)) # parametre hero sur l'écran
    parametre_hero_2(str(hero_y)) # parametre hero sur l'écran
    parametre_hero_3(str(hero_vitesse_x)) # parametre hero sur l'écran
    parametre_hero_4(str(hero_vitesse_y)) # parametre hero sur l'écran
    parametre_hero_5(str(hero_acceleration_x)) # parametre hero sur l'écran

    parametre_ennemi_1(str(ennemi_x)) # parametre ennemi sur l'écran
    parametre_ennemi_2(str(ennemi_y)) # parametre ennemi sur l'écran

    parametre_fond_ecran(str(background_x)) # parametre ennemi sur l'écran
    parametre_grenade_x(str(grenade_x)) # parametre grenade x
    parametre_grenade_y(str(grenade_y)) # parametre grenade y

    grenade(grenade_x, grenade_y, img_grenade) # La grenade sur l'écran
    balle(balle_x, balle_y, img_balle)
    hero(hero_x,hero_y,hero_img) # Le Hero sur l'écran

    # Animation Pour Hero De Gauche A Droite

    if defil<16 and ennemi_x < hero_x : # Ce gif ne marche que si l'ennemie est a gauche du hero
        defil=defil+1
    else:
        defil=1


    if defil ==1:
        ennemi(ennemi_x, ennemi_y, ennemi_img1)
    if defil ==2:
        ennemi(ennemi_x, ennemi_y, ennemi_img2)
    if defil ==3:
        ennemi(ennemi_x, ennemi_y, ennemi_img3)
    if defil ==4:
        ennemi(ennemi_x, ennemi_y, ennemi_img4)
    if defil ==5:
        ennemi(ennemi_x, ennemi_y, ennemi_img5)
    if defil ==6:
        ennemi(ennemi_x, ennemi_y, ennemi_img6)
    if defil ==7:
        ennemi(ennemi_x, ennemi_y, ennemi_img7)
    if defil ==8:
        ennemi(ennemi_x, ennemi_y, ennemi_img8)
    if defil ==9:
        ennemi(ennemi_x, ennemi_y, ennemi_img9)
    if defil ==10:
        ennemi(ennemi_x, ennemi_y, ennemi_img10)
    if defil ==11:
        ennemi(ennemi_x, ennemi_y, ennemi_img11)
    if defil ==12:
        ennemi(ennemi_x, ennemi_y, ennemi_img12)
    if defil ==13:
        ennemi(ennemi_x, ennemi_y, ennemi_img13)
    if defil ==14:
        ennemi(ennemi_x, ennemi_y, ennemi_img14)
    if defil ==15:
        ennemi(ennemi_x, ennemi_y, ennemi_img15)
    if defil ==16:
        ennemi(ennemi_x, ennemi_y, ennemi_img16)



     # Animation Pour Hero De Gauche A Droite

##    if defil<16 and ennemi_x > hero_x : # Ce gif ne marche que si l'ennemie est a droite du hero
##        defil=defil+1
##    else:
##        defil=1


##    if defil ==1:
##        ennemi(ennemi_x, ennemi_y, ennemi_img1_reverse)
##    if defil ==2:
##        ennemi(ennemi_x, ennemi_y, ennemi_img2_reverse)
##    if defil ==3:
##        ennemi(ennemi_x, ennemi_y, ennemi_img3_reverse)
##    if defil ==4:
##        ennemi(ennemi_x, ennemi_y, ennemi_img4_reverse)
##    if defil ==5:
##        ennemi(ennemi_x, ennemi_y, ennemi_img5_reverse)
##    if defil ==6:
##        ennemi(ennemi_x, ennemi_y, ennemi_img6_reverse)
##    if defil ==7:
##        ennemi(ennemi_x, ennemi_y, ennemi_img7_reverse)
##    if defil ==8:
##        ennemi(ennemi_x, ennemi_y, ennemi_img8_reverse)
##    if defil ==9:
##        ennemi(ennemi_x, ennemi_y, ennemi_img9_reverse)
##    if defil ==10:
##        ennemi(ennemi_x, ennemi_y, ennemi_img10_reverse)
##    if defil ==11:
##        ennemi(ennemi_x, ennemi_y, ennemi_img11_reverse)
##    if defil ==12:
##        ennemi(ennemi_x, ennemi_y, ennemi_img12_reverse)
##    if defil ==13:
##        ennemi(ennemi_x, ennemi_y, ennemi_img13_reverse)
##    if defil ==14:
##        ennemi(ennemi_x, ennemi_y, ennemi_img14_reverse)
##    if defil ==15:
##        ennemi(ennemi_x, ennemi_y, ennemi_img15_reverse)
##    if defil ==16:
##        ennemi(ennemi_x, ennemi_y, ennemi_img16_reverse)

# Fin de la Partie / Choix

choix = False

while not choix :

    for event in pygame.event.get():

        if event.key == pygame.K_a :

            choix = True

        if event.key == pygame.K_e :

            choix = True


    # Affichage qui reste
    background(background_x, background_y, fond_ecran)
    pygame.draw.rect(ecran,MARRON,[plateforme_lvl1_x,plateforme_lvl1_y,fenetre_longeur,fenetre_largeur]) # plateforme du niveau 1
    pygame.draw.rect(ecran,VERT,[plateforme_lvl1_x,plateforme_lvl1_y,fenetre_longeur,7.5])
    game_over("Game Over")
    game_over_options("Press A for Restart", "Press E for Quit")



pygame.display.flip()
clock.tick(60)



pygame.quit() # FIN

