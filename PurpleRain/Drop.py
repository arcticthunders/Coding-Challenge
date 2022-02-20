from p5 import *


class Drop:
    def __init__(self, x, y, yspeed) -> None:
        self.x = x
        self.y = y
        self.z = random_uniform(0, 20)
        self.length = remap(self.z, (0, 20), (5, 12))
        self.yspeed = remap(self.z, (0, 20), (4, 10))

    def fall(self):
        self.y = self.y + self.yspeed
        # self.yspeed += 0.2
        if self.y > height:
            self.x, self.y, self.yspeed = random_uniform(
                width), random_uniform(-200, 0), remap(self.z, (0, 20), (4, 10))

    def show(self):
        thick = remap(self.z, (0, 20), (1, 2))
        stroke_weight(thick)
        stroke(138, 43, 226)
        line(self.x, self.y, self.x, self.y+self.length)
