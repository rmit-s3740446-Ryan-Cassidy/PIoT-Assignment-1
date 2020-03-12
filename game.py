from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import electronicDie
import csv
import os

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
sense.show_message("End")