import pygame, math, sys
from pygame.locals import *
from datetime import datetime
white = (255,255,255)
red = (255, 0, 0)
black = (0,0,0)
size = 400.0

def roint(num):
    return int(round(num))

screen = pygame.display.set_mode((roint(size),roint(size)))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(black)
    for hour in range(12):
        cos = math.cos(math.radians(360.0 / 12 * hour))
        sin = math.sin(math.radians(360.0 / 12 * hour))
        x_h_0 = roint(size/2 + size/15*cos*4)
        y_h_0 = roint(size/2 + size/15*sin*4)
        x_h_1 = roint(size/2 + size/3*cos)
        y_h_1 = roint(size/2 + size/3*sin)
        pygame.draw.line(screen, red,[x_h_0,y_h_0],[x_h_1,y_h_1],3)
        
    for minute in range(60):
        cos = math.cos(math.radians(360.0 / 60 * minute))
        sin = math.sin(math.radians(360.0 / 60 * minute))
        x_m_0 = roint(size/2 +size/13*cos*4)
        y_m_0 = roint(size/2 + size/13*sin*4)
        x_m_1 = roint(size/2 + size/3*cos)
        y_m_1 = roint(size/2 + size/3*sin)
        pygame.draw.line(screen, red,[x_m_0 ,y_m_0],[x_m_1 ,y_m_1],2)

    second = float(datetime.now().second)
    minute = float(datetime.now().minute)
    hour = float(datetime.now().hour)
    # Second
    angle = 6 * second - 90
    x = size/2 + 9*size/30 * math.cos(math.radians(angle))
    y = size/2 + 9*size/30 * math.sin(math.radians(angle))
    pygame.draw.line(screen, white,[size/2,size/2],[x, y],3)
    # Minute Hand
    angle = 6 * minute + second/10 - 90
    x = size/2 + 8*size/30 * math.cos(math.radians(angle))
    y = size/2 + 8*size/30 * math.sin(math.radians(angle))
    pygame.draw.line(screen, white,[size/2,size/2],[x, y],5)
    # Second Hand
    angle = 30 * (hour%12) + 5*minute/10 - 90
    x = size/2 + 6*size/30 * math.cos(math.radians(angle))
    y = size/2 + 6*size/30 * math.sin(math.radians(angle))
    pygame.draw.line(screen, white,[size/2,size/2],[x, y],10)

    # The Clock
    pygame.draw.circle(screen, red, (roint(size/2), roint(size/2)),roint(size/3), 3)        

    
    pygame.display.flip()
