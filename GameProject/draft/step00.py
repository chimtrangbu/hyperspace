import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import random
from pyglet.image.codecs.png import PNGImageDecoder

# Global variables
window = pyglet.window.Window(800, 600)
label = pyglet.text.Label("0", font_size=36, y=450, x=400)
image = pyglet.image.load_animation('images/kitkat.gif')
sprite = pyglet.sprite.Sprite(img=image, x = -50)

# Event callbacks
@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()

# Game loop (loop? Why loop?)
def game_loop(_):
    label.text = str(int(label.text) + 1)

def update(dt):
    # Move 50 pixels per second
    sprite.x += 50*0.1
pyglet.clock.schedule_interval(update, 1/60.)

pyglet.clock.schedule(game_loop)
pyglet.app.run()
