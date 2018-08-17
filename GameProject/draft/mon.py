import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from random import randint


window = pyglet.window.Window(1200, 900, fullscreen = False)
monkey1 = pyglet.image.load_animation('images/minimon.gif')
monkey2 = pyglet.image.load_animation('images/mon.gif')
# monkey3 = pyglet.image.load_animation('images/maximon.gif')
gifs = [monkey1, monkey2]
# sprite1 = pyglet.sprite.Sprite(img=monkey1, y = 0)
# sprite2 = pyglet.sprite.Sprite(img=monkey2, y = 0)
# sprite3 = pyglet.sprite.Sprite(img=monkey3, y = 0)

monkeys = []
for i in range(5):
    for m in gifs:
        monkeys.append(pyglet.sprite.Sprite(m, x=randint(0,10)/10*window.width, y = 2*window.height-200*i))

@window.event
def on_draw():
    window.clear()
    # sprite.draw()
    for m in monkeys:
        m.draw()

# def update(dt):
#     for m in monkeys:
#         m.y += dt * 50
# pyglet.clock.schedule_interval(update, 1/60.)

def game_loop(dt):
    for m in monkeys:
        m.y -= dt*50
        if m.y < 0:
            monkeys.remove(m)
    if len(monkeys) < 10:
        for m in gifs:
            monkeys.append(pyglet.sprite.Sprite(m, x=randint(0,100)/100*window.width, y = window.height))
pyglet.clock.schedule(game_loop)

pyglet.app.run()
