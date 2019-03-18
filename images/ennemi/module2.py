import pygame

def hero(x,y,image):
    ecran.blit(image,(x,y))

hero_img= pygame.image.load("frame-01.png")
hero_img2= pygame.image.load("frame-02.png")
hero_img3= pygame.image.load("frame-03.png")
hero_img4= pygame.image.load("frame-04.png")
hero_img5= pygame.image.load("frame-05.png")
hero_img6= pygame.image.load("frame-06.png")
hero_img7= pygame.image.load("frame-07.png")
hero_img8= pygame.image.load("frame-08.png")
hero_img9= pygame.image.load("frame-09.png")
hero_img10= pygame.image.load("frame-10.png")
hero_img11= pygame.image.load("frame-11.png")
hero_img12= pygame.image.load("frame-12.png")
hero_img13= pygame.image.load("frame-13.png")
hero_img14= pygame.image.load("frame-14.png")
hero_img15= pygame.image.load("frame-15.png")
hero_img16= pygame.image.load("frame-16.png")



NOIR = ( 0, 0, 0)
BLANC = ( 255, 255, 255)
ROUGE = ( 255, 0, 0)
VERT = (0,255,0)

#initialisation de pygame
pygame.init()

#taille de l'ecran
taille = (600, 400)
#dessin de l'ecran
ecran = pygame.display.set_mode(taille)
#ecriture du titre
pygame.display.set_caption("bouger homme avec fleches")

# initialisation de la vitesse
x_vitesse=0
y_vitesse=0
# initialisation de la position du bonhomme
x_coord=10
y_coord=10
# initialisation de la position du bonhommeE
x_coordE=100
y_coordE=10

# initialisation de la vitesse
x_vitesseE=1
y_vitesseE=1

defil=0 # Pour l'animation de l'ennemi


finir = False

clock = pygame.time.Clock()

while not finir:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finir = True
        if event.type == pygame.KEYDOWN:

# on ajuste la vitesse
            if event.key == pygame.K_LEFT:
                x_vitesse = -5
            if event.key == pygame.K_RIGHT:
                x_vitesse = 5
                k=1
            if event.key == pygame.K_UP:
                y_vitesse = -5
            if event.key == pygame.K_DOWN:
                y_vitesse = 5

        if event.type == pygame.KEYUP:
# reinitialisation de la vitesse
            if event.key == pygame.K_LEFT:
                x_vitesse = 0
            if event.key == pygame.K_RIGHT:
                x_vitesse = 0

            if event.key == pygame.K_UP:
                y_vitesse = 0
            if event.key == pygame.K_DOWN:
                y_vitesse = 0

    x_coord = x_coord + x_vitesse
    y_coord = y_coord + y_vitesse


#effacement de l'ecran
    ecran.fill(BLANC)


##    if x_coord<0:
##        x_coord=0
##    if x_coord>586:
##        x_coord=586
##    if y_coord<0:
##        y_coord=0
##    if y_coord>370:
##        y_coord=370
##    if 290<x_coord<350 and 170<y_coord<250:
##        x_coord=x_coord-x_vitesse
##        y_coord=y_coord-y_vitesse


    if defil<16:
        defil=defil+1
    else:
        defil=1


# Dessin du bonhomme
    if defil ==1:
        hero(x_coord,y_coord,hero_img)
    if defil ==2:
        hero(x_coord,y_coord,hero_img2)
    if defil ==3:
        hero(x_coord,y_coord,hero_img3)
    if defil ==4:
        hero(x_coord,y_coord,hero_img4)
    if defil ==5:
        hero(x_coord,y_coord,hero_img5)
    if defil ==6:
        hero(x_coord,y_coord,hero_img6)
    if defil ==7:
        hero(x_coord,y_coord,hero_img7)
    if defil ==8:
        hero(x_coord,y_coord,hero_img8)
    if defil ==9:
        hero(x_coord,y_coord,hero_img9)
    if defil ==10:
        hero(x_coord,y_coord,hero_img10)
    if defil ==11:
        hero(x_coord,y_coord,hero_img11)
    if defil ==12:
        hero(x_coord,y_coord,hero_img12)
    if defil ==13:
        hero(x_coord,y_coord,hero_img13)
    if defil ==14:
        hero(x_coord,y_coord,hero_img14)
    if defil ==15:
        hero(x_coord,y_coord,hero_img15)
    if defil ==16:
        hero(x_coord,y_coord,hero_img16)


#on redessine la figure
    pygame.display.flip()
#vitesse pour redessiner de la figure
    clock.tick(20)
#on quitte pygame
pygame.quit()