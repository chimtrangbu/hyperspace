import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import random
from pyglet.image.codecs.png import PNGImageDecoder


window = pyglet.window.Window(1200, 900, fullscreen = False)
# label = pyglet.text.Label("0", font_size=36, x=300, y=450,
#                           anchor_x='center', anchor_y='center')
gif = pyglet.image.load_animation('images/kitkat.gif')
sprite = pyglet.sprite.Sprite(img=gif, x = -50)
# batch = pyglet.graphics.Batch()
# img = pyglet.image.load('images/cuteicon.png')
back = pyglet.image.load('images/back.png')
ground = pyglet.image.load('images/ground.png')
# bg_list = []
# for i in range(2):
#     bg_list.append(pyglet.sprite.Sprite(ground, x=1200*i, y=0))


# position = dict(x=img.width // 2, y=img.height // 2)

@window.event
def on_draw():
    window.clear()
    # label.draw()
    # sprite.draw()
    for b in back_list:
        b.draw()
    for g in ground_list:
        g.draw()
    # img.draw()
    # back.draw()
    # ground.draw()
    # movingbackground()
    # img.blit(position['x'], position['y'])

# window.push_handlers(pyglet.window.event.WindowEventLogger())
# def game_loop(_):
#     label.text = str(int(label.text) + 1)
#
# pyglet.clock.schedule(game_loop)


def on_key_press(symbol, modifiers):
    # print('A key was pressed')
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.RIGHT:
        position['x'] += 1
    elif symbol == key.UP:
        position['y'] += 1
    elif symbol == key.DOWN:
        position['y'] -= 1
    elif symbol == key.LEFT:
        position['x'] -= 1
    elif symbol == key.ENTER:
        print('The enter key was pressed.')
    #bla bla bla

def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        position['x'] = x
        position['y'] = y
    elif button == mouse.RIGHT:
        print('The RIGHT mouse button was pressed.')

back_list = []
ground_list = []
for i in range(2):
    back_list.append(pyglet.sprite.Sprite(back, x=0, y=1800*i))
    ground_list.append(pyglet.sprite.Sprite(ground, x=1200*i, y=0))

def movingbackground(dt):
    for e in back_list:
        e.y -= 20*0.1
        if e.y <= -back.height:
            back_list.remove(e)
            back_list.append(pyglet.sprite.Sprite(back, x = 0, y=back.height))
    for e in ground_list:
        e.x -= 50*0.1
        if e.x <= -ground.width:
            ground_list.remove(e)
            ground_list.append(pyglet.sprite.Sprite(ground, x = ground.width, y=0))

    # for bg in bg_list:
    #     bg.x -= 500*dt
    #     if bg.x < -1200+10:
    #         bg_list.remove(bg)
    #         bg_list.append(pyglet.sprite.Sprite(ground, x=1200, y=0))

def update(dt):
    # Move 50 pixels per second
    sprite.x += dt * 50
    movingbackground(dt)
# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)



pyglet.app.run()
