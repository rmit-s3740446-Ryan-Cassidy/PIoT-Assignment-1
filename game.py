from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import electronicDie
import csv
import os
import datetime

class die_game:
    sense = SenseHat()
    #Electronic die instance
    die = electronicDie.elec_die(True)

    #csv file
    filename = "winner.csv"

    #Check if file exists
    if os.path.exists(filename) == False:
        with open(filename, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Winner', 'P1 Score', 'P2 Score', 'Time'])

    #Players
    p1 = 0
    p2 = 0
    winner = None
    def start(self):
        self.sense.show_message("Game")
        while True:
            self.sense.show_message("P1 Turn")
            self.p1 += self.die.prompt()
            print(self.p1)
            if self.p1 >= 30:
                break
            self.sense.show_message("P2 Turn")
            self.p2 += self.die.prompt()
            print(self.p2)
            if self.p2 >= 30:
                break
        if self.p1 > self.p2:
            self.winner = 'p1'
            self.sense.show_message("P1 is the winner")
        else:
            self.winner = 'p2'
            self.sense.show_message("P2 is the winner")
        with open(self.filename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([self.winner, self.p1, self.p2, datetime.datetime.now()])
        self.sense.show_message("End")