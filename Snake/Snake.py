from p5 import *


class Snake:
    def __init__(self, x, y, xspeed, yspeed, scl, w, h) -> None:
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.scl = scl
        self.w = w
        self.h = h
        self.food = None
        self.total = 1
        self.tail = [(0, 0)]

    def eatFood(self):
        if dist(Vector(self.x, self.y), Vector(self.food[0], self.food[1])) < 2:
            self.total += 1
            self.tail.append((0, 0))
            return True
        else:
            return False

    def pickLocation(self):
        w = self.w
        h = self.h
        col = floor(w/self.scl-1)
        row = floor(h/self.scl-1)
        self.food = floor(random_uniform(col, 0)) * \
            self.scl, floor(random_uniform(row, 0))*self.scl

    def Collission(self):
        if (self.x, self.y) in self.tail[1:] and self.total > 1:
            return True
        else:
            return False

    def update(self):
        self.x = self.x + self.xspeed*self.scl
        self.y = self.y + self.yspeed*self.scl
        if self.total > 0:
            for i in range(self.total-1, 0, -1):
                self.tail[i] = self.tail[i-1]
            self.tail[0] = (self.x, self.y)
        if self.x == self.w:
            self.x = 0
        if self.y == self.h:
            self.y = 0
        if self.x == 0 and self.xspeed < 0:
            self.x = self.w
        if self.y == 0 and self.yspeed < 0:
            self.y = self.h

    def keyPressUpdate(self, newxspeed, newyspeed):
        self.xspeed, self.yspeed = newxspeed, newyspeed

    def show(self):
        fill(255)
        for x, y in self.tail:
            rect(x, y, 10, 10)
        text(str(self.total), 0, 0)
        # rect(self.x, self.y, 10, 10)
