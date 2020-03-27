import json
import time
import sys
import os
from sense_hat import SenseHat

class monitor_display:
    #define global variables
    red=(255,0,0)
    blue=(0,0,255)
    green=(0,255,0)
    cold_max = None
    comfortable_min = None
    comfortable_max = None
    hot_min = None
    sense = SenseHat()

    def readjson(self):
        try:
            #reading json
            with open('config.json') as f:
                data = json.load(f)

            #storing data read from json
            self.cold_max = data['cold_max']
            self.comfortable_min = data['comfortable_min']
            self.comfortable_max = data['comfortable_max']
            self.hot_min = data['hot_min']
        except Exception as e:
            print(str(e))
            self.sense.clear()
            sys.exit("Error when reading from Json. Is the Json configured correctly?")

    def start(self):
        #bool for quitting
        exit = False
        while True:
            #Accurate temperature code referenced from IoT Lecture 4
            #reading temprature from sense hat and converting to int.
            t1 = self.sense.get_temperature_from_humidity()
            t2 = self.sense.get_temperature_from_pressure()
            t_cpu = get_cpu_temp()

            # Calculates the real temperature compensating CPU heating.
            t = (t1 + t2) / 2
            t_corr = t - ((t_cpu - t) / 1.5)
            t_corr = get_smooth(t_corr)
            temp_integer_value = int(t_corr)

            #if-else to change display color as per temperature
            if(temp_integer_value <= self.cold_max):
                text_color = self.blue
            elif(temp_integer_value>self.comfortable_min and temp_integer_value<self.comfortable_max):
                text_color = self.green
            else:
                text_color = self.red
            self.sense.show_message(str(repr(temp_integer_value)),text_colour=text_color,scroll_speed=0.2)

            #check joystick events, exit if middle is pressed
            for event in self.sense.stick.get_events():
                if event.direction == 'middle' and event.action == 'released':
                    exit = True
            if exit == True:
                break
            
            #waiting for ten seconds then reading temp again
            time.sleep(10)

# Get CPU temperature.
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))

# Use moving average to smooth readings.
def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
    
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x

    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3



#Standalone testing
if __name__ == '__main__':
    md = monitor_display()
    md.readjson()
    md.start()