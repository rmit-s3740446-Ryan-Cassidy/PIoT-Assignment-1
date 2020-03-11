from sense_hat import SenseHat
import time
import random

sense = SenseHat()

#Colors
W = (255,255,255)
O = (0,0,0)
B = (0, 0, 255)

#settings
accel_limit = 1.5
display_time = 3

#die LED arrays
one =      [O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, B, B, O, O, O,
            O, O, O, B, B, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O]

two =      [B, B, O, O, O, O, O, O,
            B, B, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, B, B,
            O, O, O, O, O, O, B, B]

three =    [B, B, O, O, O, O, O, O,
            B, B, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, B, B, O, O, O,
            O, O, O, B, B, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, B, B,
            O, O, O, O, O, O, B, B]

four =     [B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B]

five =     [B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B,
            O, O, O, O, O, O, O, O,
            O, O, O, B, B, O, O, O,
            O, O, O, B, B, O, O, O,
            O, O, O, O, O, O, O, O,
            B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B]

six =      [B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B,
            O, O, O, O, O, O, O, O,
            B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B,
            O, O, O, O, O, O, O, O,
            B, B, O, O, O, O, B, B,
            B, B, O, O, O, O, B, B]

def rolldie():
    r = random.randint(1, 6)
    if r == 1:
        sense.set_pixels(one)
    elif r == 2:
        sense.set_pixels(two)
    elif r == 3:
        sense.set_pixels(three)
    elif r == 4:
        sense.set_pixels(four)
    elif r == 5:
        sense.set_pixels(five)
    elif r == 6:
        sense.set_pixels(six)

# Accelerometer measuring reference
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8
try:
    sense.clear()
    sense.show_message("Shake")
    print("Shake Pi to roll dice")
    while True:
        x, y, z = sense.get_accelerometer_raw().values()
        x1 = abs(x)
        y1 = abs(y)
        z1 = abs(z)
        if x1 > accel_limit or y1 > accel_limit or z1 > accel_limit:
            #if roll:
            rolldie()
            time.sleep(display_time)
            sense.clear()
except:
    print("Done")
    sense.clear()