from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import electronicDie
import csv
import os
import datetime

class player:
    def __init__(self, name):
        self.name = name
    name = None
    score = 0


class die_game:
    sense = SenseHat()
    #Electronic die instance
    die = electronicDie.elec_die(True)

    #csv file
    filename = "winner.csv"

    #Check if file exists
    def fileexists(self):
        if os.path.exists(self.filename) == False:
            with open(self.filename, 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Winner', 'P1 Score', 'P2 Score', 'Time'])

    #Players
    p1 = player("P1")
    p2 = player("P2")
    winner = None

    def start(self):
        try:
            self.fileexists()
            self.sense.show_message("Game")
            while True:
                self.sense.show_message(self.p1.name + " Turn")
                self.p1.score += self.die.prompt()
                print("P1 = " + str(self.p1.score))
                if self.p1.score >= 30:
                    break
                self.sense.show_message(self.p2.name + " Turn")
                self.p2.score += self.die.prompt()
                print("P2 = " + str(self.p2.score))
                if self.p2.score >= 30:
                    break
            if self.p1.score > self.p2.score:
                self.winner = self.p1.name
                self.sense.show_message(self.p1.name + " is the winner")
            else:
                self.winner = self.p2.name
                self.sense.show_message(self.p2.name + " is the winner")
            with open(self.filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([self.winner, self.p1.score, self.p2.score, datetime.datetime.now()])
            self.sense.show_message("End")
        except Exception as e:
            print(str(e))
            self.sense.clear()

#Standalone testing
if __name__ == '__main__':
    game = die_game()
    game.start()