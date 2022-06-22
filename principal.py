#! /usr/bin/env python
import pygame
import os, random, sys, math
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *


#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("El juego del Mago Goma...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #Icono de ventana
        icono = pygame.image.load("imagenes/icono.png")
        pygame.display.set_icon(icono)

        #Fondo de ventana de juego
        fondo = pygame.image.load("imagenes/fondo.jpg")
        screen.blit(fondo,(0,0))

        #Musica de Fondo.
        # pygame.mixer.init()
        pygame.mixer.music.load('sonidos/musicaFondo.mp3')
        pygame.mixer.music.play(3)

        #Carga de sonidos en general.
        sonidoLetras = pygame.mixer.Sound("sonidos/sonidoLetras.mp3")
        sonidoCorrecto = pygame.mixer.Sound("sonidos/sonidoCorrecto.mp3")
        sonidoIncorrecto = pygame.mixer.Sound("sonidos/sonidoIncorrecto.mp3")

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        palabra = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]
        archivo = open("lemario.txt","r",encoding="utf 8")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)

        #elige una al azar
        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)

        palabraEnPantallaAnterior=""
        dibujar(screen, palabra, palabraEnPantalla, puntos, segundos)

        #Seccion del juego
        estaJugando = True
        while estaJugando:
            while segundos > fps/1000:
            # 1 frame cada 1/fps segundos
                gameClock.tick(fps)
                totaltime += gameClock.get_time()

                if True:
                	fps = 3
                 
                #Buscar la tecla apretada del modulo de eventos de pygame
                for e in pygame.event.get():

                    #QUIT es apretar la X en la ventana
                    if e.type == QUIT:
                        pygame.quit()
                        return()

                    #Ver si fue apretada alguna tecla
                    if e.type == KEYDOWN:
                        sonidoLetras.play()
                        letra = dameLetraApretada(e.key)
                        palabra += letra #es la palabra que escribe el usuario
                        if e.key == K_BACKSPACE:
                            palabra = palabra[0:len(palabra)-1]
                        if e.key == K_RETURN:
                            #pasa la palabra a silabas
                            palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)
                            if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                                puntos += puntaje(palabra)
                                sonidoCorrecto.play()
                            else:
                                sonidoIncorrecto.play()
                                puntos-=1


                            #elige una al azar
                            palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)

                            palabra = ""

                segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

                #Limpiar pantalla anterior
                screen.blit(fondo,(0,0))

                #Dibujar de nuevo todo
                dibujar(screen, palabra, palabraEnPantalla, puntos, segundos)

                pygame.display.flip()

            while 1:
                #Esperar el QUIT del usuario
                for e in pygame.event.get():
                    if e.type == QUIT:
                        pygame.quit()
                        return

            archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
