import pygame
import random
import sys
import time

WIDTH = 800
HEIGHT = 600

num_bars = 10
bar_width = 20
space = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
#pygame.display.update()

def drawBar(x,height):
    pygame.draw.rect(screen,(0,0,0), (x,400,bar_width,height),0)

for i in range(num_bars):
    height = random.randint(-100,10 )
    x = (i*bar_width) + (i*space)
    drawBar(x, height)  
    
while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
