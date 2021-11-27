import Error_database
import Mqtt_comm as mqtt #Define mqtt broker in Mqtt_Com.py
import Data_database
import Voice_control
import threading

#Start communication thread
t = threading.Thread(target=mqtt.start_comm,)
t.start()

#Error_database.log_error("20-2-11","LVI190029","LV11",400)

Voice_control.say("LALO PASAME UN PANIAL")