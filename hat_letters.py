#1 /usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

import time

sense.show_letter("Y", (255, 0, 0))
time.sleep(1)

sense.show_letter("E", (0, 255, 0))
time.sleep(1)

sense.show_letter("E", (0, 0, 255))
time.sleep(1)

sense.clear()
