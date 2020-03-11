from sense_hat import SenseHat
import time

sense = SenseHat()
#Colors
G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
O = (0,0,0)
P = (255,105, 180)

first = [O, O, O, B, O, O, O, O,
            O, O, B, B, O, O, O, O,
            O, B, O, B, O, O, O, O,
            B, O, O, B, B, B, B, B,
            B, O, O, B, B, B, B, B,
            O, B, O, B, O, O, O, O,
            O, O, B, B, O, O, O, O,
            O, O, O, B, O, O, O, O]

second = [O, O, O, G, G, O, O, O,
            O, O, G, O, O, G, O, O,
            O, G, O, O, O, O, G, O,
            G, G, G, G, G, G, G, G,
            O, O, O, G, G, O, O, O,
            O, O, O, G, G, O, O, O,
            O, O, O, G, G, O, O, O,
            O, O, O, G, G, O, O, O]

third = [O, O, O, O, Y, O, O, O,
            O, O, O, O, Y, Y, O, O,
            O, O, O, O, Y, O, Y, O,
            Y, Y, Y, Y, Y, O, O, Y,
            Y, Y, Y, Y, Y, O, O, Y,
            O, O, O, O, Y, O, Y, O,
            O, O, O, O, Y, Y, O, O,
            O, O, O, O, Y, O, O, O]

sense.set_pixels(first)
time.sleep(3)
sense.set_pixels(second)
time.sleep(3)
sense.set_pixels(third)
time.sleep(3)
sense.clear()
quit()