import pygletfrom pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import random


label = pyglet.text.Label("0", font_size=36, x=300, y=450,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()

def update(dt):
    if ####:
        label.text = str(int(label.text) + 1)
