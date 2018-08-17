import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
import random

window = pyglet.window.Window()

# img = pyglet.image.load('images/cuteicon.png')

class main(pyglet.window.Window):
    def __init__ (self):
        super(main, self).__init__(1200, 900, fullscreen = False)
        self.alive = 1

        self.back = pyglet.sprite.Sprite(pyglet.image.load('images/back.png'))
        self.ground = pyglet.sprite.Sprite(pyglet.image.load('images/ground.png'))

        self.back.x = 0
        self.back.y = 0

        self.ground.x = 0
        self.ground.y = 0

    x = [-1,1]

    # def game_loop(self):
    #     self.back.y = -450 + i*450
    #     ###############
    #
    # pyglet.clock.schedule(game_loop)

    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def render(self):
        self.clear()

        self.back.draw()
        self.ground.draw()

        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()

def update(dt):
    # Move 50 pixels per second
    back.y += dt * 50
    ground.x += dt * 50
# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

x = main()
x.run()
