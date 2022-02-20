from p5 import *
from Drop import Drop

d = [None for _ in range(100)]


def setup():
    global d
    w = 320
    h = 160
    size(w, h)
    for i in range(len(d)):
        d[i] = Drop(random_uniform(w), random_uniform(-100, 0),
                    random_uniform(4, 10))


def draw():
    global d
    background(230, 230, 250)
    for i in range(len(d)):
        d[i].show()
        d[i].fall()


run()
