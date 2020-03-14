import json
from sense_hat import SenseHat

#reading temprature from sense hat and converting to int.
sense = SenseHat()
temp = sense.get_temperature()
temp_integer_value = int(temp)

#reading json
with open('config.json') as f:
  data = json.load(f)

#storing data read from json
cold_max = data['cold_max']
comfortable_min = data['comfortable_min']
comfortable_max = data['comfortable_max']
hot_min = data['hot_min']

# define colours
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

#if-else to change display color as per temperature
if(temp_integer_value <= cold_max):
    text_color = blue
elif(temp_integer_value>comfortable_min and temp_integer_value<comfortable_max):
    text_color = green
else:
    text_color = red

sense.show_message(str(repr(temp_integer_value)),text_colour=text_color,scroll_speed=0.2)