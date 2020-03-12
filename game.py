from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import electronicDie
import csv
import os
import datetime

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

sense.show_message("Game")
while True:
    sense.show_message("P1 Turn")
    p1 += die.prompt()
    print(p1)
    if p1 >= 30:
        break
    sense.show_message("P2 Turn")
    p2 += die.prompt()
    print(p2)
    if p2 >= 30:
        break
if p1 > p2:
    winner = 'p1'
    sense.show_message("P1 is the winner")
else:
    sense.show_message("P2 is the winner")
with open(filename, 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([winner, p1, p2, datetime.datetime.now()])
sense.show_message("End")