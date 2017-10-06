import music
from microbit import *

def check_click():
    while not button_a.is_pressed():
        sleep(1)
    while button_a.is_pressed():
        sleep(1)

while True:
    display.show(Image.HEART)
    music.play(music.NYAN)
    check_click()
    
    display.show(Image.CHESSBOARD)
    music.play(music.FUNK)
    check_click()
    
    display.show(Image.SILLY)
    music.play(music.BADDY)
    check_click()
    
    