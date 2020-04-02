from sense_hat import SenseHat
import time

class AnimatedEmoji:
    sense = SenseHat()
    #Colors
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    white = (255,255,255)
    black = (0,0,0)
    pink = (255,105, 180)
    cobalt = (61,89,171)
    brown = (165,42,42)
    golden = (238,201,0)

    happy_emoji = [black, black, black, black, black, black, black, black,
                black, green, green, black, black, green, green, black,
                black, black, black, black, black, black, black, black,
                black, black, black, yellow, yellow, black, black, black,
                black, blue, black, black, black, black, blue, black,
                black, black, blue, blue, blue, blue, black, black,
                black, black, black, black, black, black, black, black,
                black, black, black, black, black, black, black, black]

    sad_emoji = [black, black, black, black, black, black, black, black,
                black, red, red, black, black, red, red, black,
                black, black, black, black, black, black, black, black,
                black, black, black, pink, pink, black, black, black,
                black, black, black, black, black, black, black, black,
                black, black, white, white, white, white, black, black,
                black, white, black, black, black, black, white, black,
                black, black, black, black, black, black, black, black]

    poker_emoji = [black, black, black, black, black, black, black, black,
                black, cobalt, cobalt, black, black, cobalt, cobalt, black,
                black, black, black, black, black, black, black, black,
                black, black, black, brown, brown, black, black, black,
                black, black, black, black, black, black, black, black,
                black, golden, golden, golden, golden, golden, golden, black,
                black, black, black, black, black, black, black, black,
                black, black, black, black, black, black, black, black]
                
    def display(self):
        self.sense.set_pixels(self.happy_emoji)
        time.sleep(3)
        self.sense.set_pixels(self.sad_emoji)
        time.sleep(3)
        self.sense.set_pixels(self.poker_emoji)
        time.sleep(3)
        self.sense.clear()