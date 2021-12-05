import Error_database
import Mqtt_comm as mqtt #Define mqtt broker in Mqtt_comm.py
import Data_database
import Voice_control
import threading

#Start communication thread
t = threading.Thread(target=mqtt.start_comm,)
t.start()

#Data_database.log_data("20-2-11","TMP-1","90%","45")

Voice_control.say("System armed")