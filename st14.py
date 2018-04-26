import time
import RPi.GPIO as GPIO
import pygame, sys, os
import iniPi
import sqlPi
import ipPi
import timePi

from pygame.locals import *
from iniPi import * 

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
# 2 put in iniPi
icO=pygame.image.load(ic16PathS+ "power-standby" +ic16PathE)
icRect=pygame.image.load(ic16PathS+ "camera-slr" +ic16PathE)
icTri=pygame.image.load(ic16PathS+ "transfer" +ic16PathE)
icX=pygame.image.load(ic16PathS+ "cog" +ic16PathE)
icUp=pygame.image.load(ic16PathS+ "lightbulb" +ic16PathE)
icDown=pygame.image.load(ic16PathS+ "menu" +ic16PathE)
rayFace =pygame.image.load("/home/pi/pjtSmScr/icon/raymond.png")
splashScr =pygame.image.load("/home/pi/pjtSmScr/wp/coplandOS.jpg")
#pygame.mouse.set_visible(False)
DISPLAYSURF = pygame.display.set_mode((scrWidth, scrHeigth))

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.OUT)

fontSel=pygame.font.SysFont(iniPi.font, iniPi.font_size)

# DISPLAYSURF.fill(iniPi.WHITE)
# pygame.display.update()
GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)
DISPLAYSURF.blit(splashScr, (0, 0))
pygame.display.update()
time.sleep(3)
while True:
        os.system('clear')
        #DISPLAYSURF.blit(splashScr, (0, 0))
	#pygame.display.update()
        #time.sleep(30)
        DISPLAYSURF.fill(iniPi.WHITE)
        pygame.display.update()
	#default display
        #menuTxtRect= fontSel.render(menuRect, True, iniPi.font_color)
        menuTxtRect = fontSel.render(sqlPi.reqMenu("name", "rect", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)
        menuTxtX= fontSel.render(sqlPi.reqMenu("name", "croix", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)
        menuTxtTri= fontSel.render(sqlPi.reqMenu("name", "tri", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)        
        # button 1 fct only (shutdown)
        menuTxtUp= fontSel.render(sqlPi.reqMenu("name", "up", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)
        menuTxtDw= fontSel.render(sqlPi.reqMenu("name", "down", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)

        #screen
        DISPLAYSURF.blit(icO, (icOPosX, icOPosY))
        DISPLAYSURF.blit(icRect, (icRectPosX, icRectPosY))
        DISPLAYSURF.blit(icTri, (icTriPosX, icTriPosY))
        DISPLAYSURF.blit(icX, (icXPosX, icXPosY))
        DISPLAYSURF.blit(icDown, (icDownPosX, icDownPosY))
        DISPLAYSURF.blit(icUp, (icUpPosX, icUpPosY))
        DISPLAYSURF.blit(rayFace, (34, 0))
        
        pygame.display.flip()

        if (not GPIO.input(5)):
                # X
                clkX+=1
                # pygame.display.update()
        if (not GPIO.input(22)):
                # rect
                clkRect+=1
                #pygame.display.update()
        if (not GPIO.input(23)):
                # O
                pygame.quit()
                sys.exit()
        if (not GPIO.input(24)):
                # triangle
                clkTri+=1
                #pygame.display.update()
        if (not GPIO.input(4)):
                #VOL LOW
                clkDown+=1
                #GPIO.output(27,GPIO.HIGH)
        if (not GPIO.input(17)):
                #VOL HIGH
                clkUp+=1
                #GPIO.output(27,GPIO.LOW)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        time.sleep(0.1)
