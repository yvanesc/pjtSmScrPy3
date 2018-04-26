import pygame
import os

os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()
picture=pygame.image.load("/home/pi/pjtSmScr/wp/coplandOS.jpg")
pygame.display.set_mode(picture.get_size())
main_surface = pygame.display.get_surface()
main_surface.blit(picture, (0,0))
while True:
   main_surface.blit(picture, (0,0))
   pygame.display.update()
