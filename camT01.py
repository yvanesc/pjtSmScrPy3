import pygame.camera
#import picamera
#import asciiNbr
#import asciiTxt

# backslash remove space before & after multiline

#camera = picamera.PiCamera()
width = 640
height = 480
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width, height))#/home/pi/pjtSmScr",(width, height))
cam.start()
#setup window
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption('Camera')

#take pic
image = cam.get_image()
cam.stop

#save it
pygame.image.save(windowSurfaceObj,'picture2.jpg')

