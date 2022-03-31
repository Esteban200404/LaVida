from turtle import width
import pygame
import numpy as np
import time

pygame.init()

width, height = 1000 , 1000
Screen =  pygame.display.set_mode((height,width))

#color del fondo elegido
bg = 25 , 25 , 25
Screen.fill(bg)

#Numero de celdas
nxC , nyC = 27, 27

#Dimenciones de la celda
dimCW = width / nxC
dimCH = height / nyC

#Estado de las celdas vivas =1
gameState = np.zeros((nxC,nyC))

#Automata palo
gameState[10,3]=1
gameState[10,4]=1
gameState[10,5]=1

#movil
gameState[21,21]=1
gameState[22,22]=1
gameState[22,21]=1
gameState[21,23]=1
gameState[21,23]=1
#pausa del juego
pauseExect=False
#Bucle de Ejecucion
while True:

    newGameState = np.copy(gameState)

    Screen.fill(bg)

    time.sleep(0.1)

    #registro de eventos teclado y mouse
    ev=pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
            #deteccion del raton
        mouseClick= pygame.mouse.get_pressed()
        if sum(mouseClick)>0:
            posX , posY = pygame.mouse.get_pos()
            celX , celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX,celY]= not mouseClick[2]

    for y in range(0,nxC):
        for x in range(0,nyC):

            if not pauseExect:
                #calculo del numero de vecinos cercanos
                n_neigt = gameState[(x-1) %nxC, (y-1) % nyC] + \
                        gameState[(x) %nxC, (y-1) % nyC ] + \
                        gameState[(x+1) %nxC, (y-1)  % nyC] + \
                        gameState[(x-1) %nxC, (y) % nyC]  + \
                        gameState[(x+1) %nxC, (y) % nyC] + \
                        gameState[(x-1) %nxC, (y+1) % nyC] + \
                        gameState[(x) %nxC, (y+1) % nyC] + \
                        gameState[(x+1) %nxC, (y+1) % nyC] 
                #celula muerta con 3 celdas vivas, revive
                if gameState[x,y] == 0 and n_neigt ==3:
                    newGameState[x,y] = 1
                #celula viva con menos de 2 o mas de 3 vecinas vivas, muere
                elif gameState[x,y]==1 and (n_neigt<2 or n_neigt>3):
                    newGameState[x,y] = 0
                #poligono de cada celda a dibujar
            poly =  [((x)  * dimCW, y     * dimCH),
                    ((x+1) * dimCW, y     * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH), 
                    ((x)   * dimCW, (y+1) * dimCH)]
                #dibujar la celda para cada par de x e y
            if newGameState[x,y] == 0:
                pygame.draw.polygon(Screen,(128, 128, 128),poly,1)
            else:
        
                pygame.draw.polygon(Screen,(255, 255, 255),poly,0)
                #actualizar el estado del juego 
    gameState = np.copy(newGameState)
                #actualiza la pantalla 
    pygame.display.flip()
    pass