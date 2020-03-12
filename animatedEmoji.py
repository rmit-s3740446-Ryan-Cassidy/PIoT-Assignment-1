from sense_hat import SenseHat
import time

class AnimatedEmoji:
    sense = SenseHat()
    #Colors
    G = (0, 255, 0)
    Y = (255, 255, 0)
    B = (0, 0, 255)
    R = (255, 0, 0)
    W = (255,255,255)
    O = (0,0,0)
    P = (255,105, 180)
    CB = (61,89,171)
    BR = (165,42,42)
    GO = (238,201,0)

    happy_emoji = [O, O, O, O, O, O, O, O,
                O, G, G, O, O, G, G, O,
                O, O, O, O, O, O, O, O,
                O, O, O, Y, Y, O, O, O,
                O, B, O, O, O, O, B, O,
                O, O, B, B, B, B, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O]

    sad_emoji = [O, O, O, O, O, O, O, O,
                O, R, R, O, O, R, R, O,
                O, O, O, O, O, O, O, O,
                O, O, O, P, P, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, W, W, W, W, O, O,
                O, W, O, O, O, O, W, O,
                O, O, O, O, O, O, O, O]

    poker_emoji = [O, O, O, O, O, O, O, O,
                O, CB, CB, O, O, CB, CB, O,
                O, O, O, O, O, O, O, O,
                O, O, O, BR, BR, O, O, O,
                O, O, O, O, O, O, O, O,
                O, GO, GO, GO, GO, GO, GO, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O]
                
    def display(self):
        self.sense.set_pixels(self.happy_emoji)
        time.sleep(3)
        self.sense.set_pixels(self.sad_emoji)
        time.sleep(3)
        self.sense.set_pixels(self.poker_emoji)
        time.sleep(3)
        self.sense.clear()
        quit()