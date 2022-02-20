from matplotlib import fontconfig_pattern
from p5 import *
from Snake import Snake

s = None
scl = None
food = None


def setup():
    w = 640
    h = 360
    size(w, h)
    global s, scl, food
    scl = 10
    s = Snake(0, 0, 1, 0, scl, w, h)
    s.pickLocation()


def draw():
    global s, food
    background(0)
    keyPressed()
    if s.Collission():
        text('GAME OVER!!', floor(s.w//2), floor(s.h//2))
        text('Score:' + str(s.total), floor(s.w//2), floor(s.h//2) + 2*s.scl)
        no_loop()
    if s.eatFood():
        s.pickLocation()
    s.update()
    fill(255, 0, 100)
    rect(s.food[0], s.food[1], scl, scl)

    s.show()


def keyPressed():
    global s
    speed = max(abs(s.xspeed), abs(s.yspeed))
    if key_is_pressed:
        if key == 'DOWN':
            s.keyPressUpdate(0, speed)
        elif key == "UP":
            s.keyPressUpdate(0, -1*speed)
        elif key == "LEFT":
            s.keyPressUpdate(-1*speed, 0)
        elif key == "RIGHT":
            s.keyPressUpdate(speed, 0)
        print(s.x)


run(frame_rate=10)
