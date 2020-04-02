from sense_hat import SenseHat
from signal import pause
from time import sleep
import animatedEmoji
import monitorAndDisplay
import game

sense = SenseHat()
animate = animatedEmoji.AnimatedEmoji()
temp = monitorAndDisplay.MonitorDisplay()
game = game.DieGame()


def task_one():
    print("Task One")
    animate.display()


def task_two():
    print("Task Two")
    temp.read_json()
    temp.start()


def task_three():
    print("Task Three")
    game.file_exists()
    game.start()


def end_program():
    sense.clear()
    print("Quitting")
    quit()


while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "left":
                task_one()
            elif event.direction == "up":
                task_two()
            elif event.direction == "right":
                task_three()
            elif event.direction == "down":
                end_program()
            sense.stick.get_events().clear()
            sleep(0.5)
