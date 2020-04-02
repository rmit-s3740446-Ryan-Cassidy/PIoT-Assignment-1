from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import electronicDie
import csv
import os
import datetime
import traceback


class player:
    def __init__(self, name):
        self.name = name

    name = None
    score = 0


class DieGame:
    sense = SenseHat()
    # Electronic die instance
    die = electronicDie.ElectronicDie(True)

    # csv file
    filename = "winner.csv"

    # Check if winner.csv exists
    def file_exists(self):
        if os.path.exists(self.filename) == False:
            with open(self.filename, "w") as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
                )
                writer.writerow(["Winner", "P1 Score", "P2 Score", "Time"])

    # Players
    p1 = player("P1")
    p2 = player("P2")
    winner = None

    # Game start
    def start(self):
        exit = False
        try:
            # Check for winner.csv
            self.file_exists()

            # Display instructions
            self.sense.show_message("Take turns rolling dice by shaking Pi")
            self.sense.show_message("First player to 30 wins")

            # Loop player turns till one players score >= 30
            while True:
                self.sense.show_message(
                    self.p1.name + " Turn, " + str(self.p1.score) + " points"
                )
                self.p1.score += self.die.prompt()
                print("P1 = " + str(self.p1.score))
                if self.p1.score >= 30:
                    self.endgame()
                    break
                self.sense.show_message(
                    self.p2.name + " Turn, " + str(self.p2.score) + " points"
                )
                self.p2.score += self.die.prompt()
                print("P2 = " + str(self.p2.score))
                if self.p2.score >= 30:
                    self.endgame()
                    break

                # check joystick events, exit if middle is pressed
                events = self.sense.stick.get_events()
                if len(events) > 0:
                    if events[-1].direction == "middle":
                        exit = True
                if exit == True:
                    self.p1.score = 0
                    self.p2.score = 0
                    break
        except Exception as e:
            print(str(e))
            traceback.print_exc()
            self.sense.clear()

    def endgame(self):
        # Determine winner
        if self.p1.score > self.p2.score:
            self.winner = self.p1.name
            self.sense.show_message(self.p1.name + " is the winner")
        else:
            self.winner = self.p2.name
            self.sense.show_message(self.p2.name + " is the winner")

        # Record game information to winner.csv
        with open(self.filename, "a") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(
                [self.winner, self.p1.score, self.p2.score, datetime.datetime.now()]
            )
        self.sense.show_message("End")


# Standalone testing
if __name__ == "__main__":
    game = DieGame()
    game.file_exists()
    game.start()
