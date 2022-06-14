import pygame
import random
import sys
import time

WIDTH = 800
HEIGHT = 600

num_bars = 80
bar_width = 4
space = 5
bars = []
arr = []

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((0,0,0))

def bubblesort(bars):
    
    for i in range(len(bars)):
        for j in range(len(bars)-1-i):
            if(bars[j]>bars[j+1]):
                bars[j] , bars[j+1] = bars[j+1] , bars[j]
            screen.fill((0,0,0))
            for k in range(len(bars)):
                x = (k*bar_width) + (k*space) + (WIDTH -(num_bars + bar_width + num_bars + space))/15
                drawBar(x,bars[k])
            pygame.display.update()
            time.sleep(0.02)



#def button(msg,x,y,w,h,ic,ac):
    

def drawBar(x,height):
    pygame.draw.rect(screen,(250,250,255), (x,80,bar_width,height),0)
    #bars.append(height)

for i in range(num_bars):
    height = random.randint(25,485 )
    bars.append(height)
    x = (i*bar_width) + (i*space) + (WIDTH -(num_bars + bar_width + num_bars + space))/5
    drawBar(x, height)  

#pygame.display.update()    
while True:
    pygame.display.update()

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       bubblesort(bars)    
