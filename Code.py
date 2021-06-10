import pygame
import random
import sys
import time

WIDTH = 800
HEIGHT = 600

num_bars = 20
bar_width = 15
space = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((0,0,0))

def button(msg,x,y,w,h,ic,ac):
    

def drawBar(x,height):
    pygame.draw.rect(screen,(255,255,255), (x,200,bar_width,height),0)

for i in range(num_bars):
    height = random.randint(20,200 )
    x = (i*bar_width) + (i*space) + (WIDTH -(num_bars + bar_width + num_bars + space))/3.5
    drawBar(x, height)  
    
while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
