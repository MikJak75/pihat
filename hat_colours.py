#1 /usr/bin/env python

from sense_hat import SenseHat 

sense = SenseHat()

pink = (255,0,127)

speed = 0.05

message = "YEEEEEE      8======================================D~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EEEEEEEEEEEEEE!"

sense.show_message(message, speed, pink, (0,255,0))

sense.clear()
