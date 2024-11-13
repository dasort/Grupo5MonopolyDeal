import pygame
import sys

pygame.init()

#config de la pantalla de inicio 
ANCHO = 850
ALTO = 800

pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Pantalla inicial")

imagen_menu = pygame.image.load("vista/menudeprueba.png")
boton_img = pygame.image.load("vista/boton.png")

imagen_menu = pygame.transform.scale(imagen_menu, (ANCHO, ALTO))

boton_img = pygame.transform.scale(boton_img, (360, 90))

boton_rect = boton_img.get_rect(center=(ANCHO // 2, ALTO // 2))


#def nueva_partida():
#    pass
#
#def crear_usuario():
#    pass
#
#def inicio_sesion():
#    pass 


def menu_inicio ():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    #acciones de los 3 botones que tenemos, nueva_partida, inicio_sesion etc
                    pass

        pantalla.blit(imagen_menu, (0, 0))
        pantalla.blit(boton_img, boton_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

menu_inicio()

