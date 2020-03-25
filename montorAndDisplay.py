import json
import time
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

    def start(self):
        while True:
            #reading temprature from sense hat and converting to int.
            temp = self.sense.get_temperature()
            temp_integer_value = int(temp)

            #if-else to change display color as per temperature
            if(temp_integer_value <= self.cold_max):
                text_color = self.blue
            elif(temp_integer_value>self.comfortable_min and temp_integer_value<self.comfortable_max):
                text_color = self.green
            else:
                text_color = self.red
            self.sense.show_message(str(repr(temp_integer_value)),text_colour=text_color,scroll_speed=0.2)

            #waiting for ten seconds then reading temp again
            time.sleep(10)

#Standalone testing
if __name__ == '__main__':
    md = monitor_display()
    md.readjson()
    md.start()