from sense_hat import SenseHat
from signal import pause
from time import sleep
import animatedEmoji
import monitorAndDisplay
import game

sense = SenseHat()
animate = animatedEmoji.AnimatedEmoji()
temp = monitorAndDisplay.monitor_display()
game = game.die_game()

def taskone():
    print("Task One")
    animate.display()

def tasktwo():
    print("Task Two")
    temp.readjson()
    temp.start()

def taskthree():
    print("Task Three")
    game.fileexists()
    game.start()

def endprogram():
    sense.clear()
    print("Quitting")
    quit()

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "left":
                taskone()
            elif event.direction == 'up':
                tasktwo()
            elif event.direction == 'right':
                taskthree()
            elif event.direction == 'down':
                endprogram()
            sense.stick.get_events().clear()
            sleep(0.5)