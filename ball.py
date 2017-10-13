# Add your Python code here. E.g.
from microbit import *

import random
V = 25
def get_random_v():
    return random.randrange(20, 25)*random.choice([1, -1])

class Ball():

    def __init__(self):
        self.x = random.randrange(100, 400)
        self.vx = get_random_v()
        self.y = random.randrange(100, 400)
        self.vy = get_random_v()
    
    def force(self):
        self.vx = get_random_v()
        self.vy = get_random_v()
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > 450:
            self.vx *= -0.9
            self.x = 450
        if self.x < 50:
            self.vx *= -0.9
            self.x = 50
        if self.y > 450:
            self.vy *= -0.9
            self.y = 450
        if self.y < 50:
            self.vy *= -0.9
            self.y = 50
balls = []

for i in range(5):
    balls.append( Ball() )


while True:
        display.clear()
        for ball in balls:
            ball.move()
            #canvas.draw_image(image, (500 / 2, 500 / 2), (500, 500), (ball.x, ball.y), (100, 100))
            display.set_pixel(int(ball.x/100), int(ball.y/100), 9)
        sleep(10)
        if accelerometer.was_gesture("shake"):
            for ball in balls:
                ball.force()