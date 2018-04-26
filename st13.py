import time
import RPi.GPIO as GPIO
import pygame, sys, os
import iniPi
import sqlPi
import ipPi
import timePi

from pygame.locals import *
from iniPi import * #clkX, clkRect, clkTri, clkUp, clkDw, pathStart, pathEnd, scrWidth, scrHeigth, icOPosX, icOPosY, icRectPosX, icRectPosY

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
# 2 put in iniPi
icO=pygame.image.load(pathStart+ "power-standby" +pathEnd)#wp/coplandOS.jpg")
icRect=pygame.image.load(pathStart+ "camera-slr" +pathEnd)
icTri=pygame.image.load(pathStart+ "transfer" +pathEnd)
icX=pygame.image.load(pathStart+ "cog" +pathEnd)
icUp=pygame.image.load(pathStart+ "lightbulb" +pathEnd)
#icDown=pygame.image.load(pathStart+ "menu" +pathEnd)
# test small icon 16x16
icDown=pygame.image.load("/home/pi/pjtSmScr/ic16/menu-2x.png")
rayFace =pygame.image.load("/home/pi/pjtSmScr/icon/raymond.png")
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

DISPLAYSURF.fill(iniPi.WHITE)
pygame.display.update()
GPIO.output(27,GPIO.HIGH)
pygame.mouse.set_visible(False)

while True:
        os.system('clear')
        DISPLAYSURF.fill(iniPi.WHITE)
        #default display
        #fontSel=pygame.font.SysFont(font, font_size)
        #menuTxtRect= fontSel.render(menuRect, True, iniPi.font_color)
        menuTxtRect = fontSel.render(sqlPi.reqMenu("name", "rect", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)
        menuTxtX= fontSel.render(sqlPi.reqMenu("name", "croix", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)
        menuTxtTri= fontSel.render(sqlPi.reqMenu("name", "tri", str(clkRect), str(clkTri), str(clkX), str(clkUp), str(clkDw)), True, iniPi.font_color)        
        # button 1 fct only (shutdown)
        menuTxtO= fontSel.render("<- ShutDown", True, iniPi.font_color)        
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
        
        #display red rect to be calculate
        #pygame.draw.rect(DISPLAYSURF, iniPi.RED, (160, 25, 150, 190)) x, y, width, height
        # only marge not enough
        #pygame.draw.rect(DISPLAYSURF, iniPi.RED, (widthMax + iniPi.marge +5, 25, 360 - widthMax , 190))
        # display info in red square
        #infoTxt = fontSel.render("Ip wifi: " + ipPi.get_ip_address('wlan0'), True, iniPi.WHITE)
        # need to add try + except in ipPi
        #infoTxt2 = fontSel.render("Ip wire: " + ipPi.get_ip_address('eth0'), True, iniPi.WHITE)
        #infoTxt2 = fontSel.render(timePi.timePi + " | "+ timePi.dayOfWeek, True, iniPi.WHITE)
        #DISPLAYSURF.blit(infoTxt, (widthMax + iniPi.marge +5, 25))
        #heightInfoTxt = infoTxt.get_rect().height
        #DISPLAYSURF.blit(infoTxt2, (widthMax + iniPi.marge +5, 25+heightInfoTxt))
        #infoTxt3 = fontSel.render(timePi.nowMonth + " "+ timePi.nbMonth + " " + timePi.nowYear, True, iniPi.WHITE)
        #DISPLAYSURF.blit(infoTxt3, (widthMax + iniPi.marge +5, 25+(heightInfoTxt*2)))
        pygame.display.flip()

        #pygame.display.update()
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
