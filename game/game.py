import pygame as pG
import sys

x = 600
y = 750
pG.init()
screen = pG.display.set_mode((x,y))

def draw_snake():
    pass

while True:
    pG.display.update()

    for event in pG.event.get():
        if event.type == pG.QUIT:
            pG.quit()
            sys.exit()