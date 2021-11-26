import Error_database
import Mqtt_comm as mqtt #Define mqtt broker in Mqtt_Com.py
import Voice_control

mqtt.start_comm()
#Error_database.log_error("20-2-11","LVI190029","LV11",400)
#mqtt.send_message("topicExample","messageExample")
Voice_control.say("LALO PASAME UN PANIAL")