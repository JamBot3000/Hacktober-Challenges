import pygame,sys
from math import cos,sin
from pygame.locals import *
import random

pygame.init()

fps=15
fpsClock=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((1280,780),0,32)
pygame.display.set_caption("Animated Design ")
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
cr=(220,255,250)

#tree=pygame.draw.circle(DISPLAYSURF,blue,(223,257),20,4)

n=[blue,green,black,red]
x=0


while True:
    DISPLAYSURF.fill(cr)

    fontobj=pygame.font.Font('freesansbold.ttf',22)
    textobj=fontobj.render('ishank agarwal',True,green,blue)
    textrectobj=textobj.get_rect()
    textrectobj.center=(1000,700)
    x_new=900
    y_new=600
    rad=200
    for i in range(1,360):

        pygame.draw.circle(DISPLAYSURF,n[x],(x_new,y_new),rad,1)
        
        pygame.draw.circle(DISPLAYSURF,n[x],(int(280-150*cos(i)),int(550-150*sin(i))),100,1)
        x=x+1;
        x_new=x_new-4
        y_new=y_new-4
        rad=rad-2
        if (x==4):
            x=0
        if x_new==100 or y_new==100:
            x_new=900
            y_new=600
        if rad==4:
            rad=200
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(fps)
