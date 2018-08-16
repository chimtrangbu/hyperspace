import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import random


window = pyglet.window.Window()
label = pyglet.text.Label("0", font_size=36, x=300, y=450,
                          anchor_x='center', anchor_y='center')
image = pyglet.image.load_animation('images/kitkat.gif')
sprite = pyglet.sprite.Sprite(img=image, x = -50)
batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()

window.push_handlers(pyglet.window.event.WindowEventLogger())
def game_loop(_):
    label.text = str(int(label.text) + 1)

pyglet.clock.schedule(game_loop)

def on_key_press(symbol, modifiers):
    # print('A key was pressed')
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.RIGHT:
        print('The RIGHT arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')
    #bla bla bla

bg_list = []
for i in range(2):
    bg_list.append()

def update(dt):
    # Move 50 pixels per second
    sprite.x += dt * 50
# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)


def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    elif button == mouse.RIGHT:
        print('The RIGHT mouse button was pressed.')



pyglet.app.run()
