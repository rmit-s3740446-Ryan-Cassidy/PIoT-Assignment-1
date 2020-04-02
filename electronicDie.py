from sense_hat import SenseHat
import time
import random
#Set game_mode to True for single roll returning value
#False for demonstration purposes
class ElectronicDie:
    def __init__(self, mode):
        self.game_mode = mode
    sense = SenseHat()

    #Colours
    O = (0,0,0)
    B = (0, 0, 255)

    #Settings
    #game_mode setting determines if dice will roll infinitely (Used for testing)
    accel_limit = 1.5
    display_time = 3
    game_mode = False

    #Die LED arrays
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

    #Roll function
    def roll_die(self):
        r = random.randint(1, 6)
        if r == 1:
            self.sense.set_pixels(self.one)
        elif r == 2:
            self.sense.set_pixels(self.two)
        elif r == 3:
            self.sense.set_pixels(self.three)
        elif r == 4:
            self.sense.set_pixels(self.four)
        elif r == 5:
            self.sense.set_pixels(self.five)
        elif r == 6:
            self.sense.set_pixels(self.six)
        return r

    #Accelerometer measuring reference
    #https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/8
    #Prompt for shaking to roll
    def prompt(self):
        try:
            self.sense.clear()
            self.sense.show_message("Shake")
            print("Shake Pi to roll dice")
            while True:
                x, y, z = self.sense.get_accelerometer_raw().values()
                x1 = abs(x)
                y1 = abs(y)
                z1 = abs(z)
                if x1 > self.accel_limit or y1 > self.accel_limit or z1 > self.accel_limit:
                    r = self.roll_die()
                    time.sleep(self.display_time)
                    self.sense.clear()
                    if self.game_mode == True:
                        return r
        except Exception as e:
            print(str(e))
            self.sense.clear()

#Standalone testing
if __name__ == '__main__':
    die = ElectronicDie(False)
    die.prompt()