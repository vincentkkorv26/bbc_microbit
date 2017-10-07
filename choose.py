from microbit import *
import random

one = Image("00900:"
            "09900:"
            "00900:"
            "00900:"
            "09990")
              
two = Image("00990:"
            "09009:"
            "00090:"
            "00900:"
            "09999")
              
three = Image("00900:"
              "09090:"
              "00900:"
              "09090:"
              "00900:")
              
four = Image("09090:"
             "09090:"
             "09999:"
             "00090:"
             "00090:")
              
five = Image("09990:"
             "09000:"
             "09990:"
             "00090:"
             "09990:")
             
six = Image("09990:"
            "09000:"
            "09990:"
            "09090:"
            "09990:")
            
seven = Image("09990:"
              "09090:"
              "00090:"
              "00090:"
              "00090:")
              
eight = Image("09990:"
              "09090:"
              "09990:"
              "09090:"
              "09990:")
              
nine = Image("09990:"
             "09090:"
             "09990:"
             "00090:"
             "09990:")
             
ten = Image("90999:"
            "90909:"
            "90909:"
            "90909:"
            "90999:")
              

numbers = [one, two, three, four, five, six, seven, eight, nine, ten]

while True:
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.show(random.choice(numbers))
    sleep(10)
