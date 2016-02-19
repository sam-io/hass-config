import bluetooth
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = '192.168.1.5'
loc_dani = 'hass/dani/localizacion'
loc_ana = 'hass/ana/localizacion'

client = mqtt.Client("hass-client-2")
client.connect(broker)
#client.loop_start()

result = bluetooth.lookup_name(<mac_iphone>, timeout=5)
if (result != None):
	client.publish(loc_dani, 'home', retain=True)
else:
	client.publish(loc_dani, 'not_home', retain=True)
result = bluetooth.lookup_name(<mac_galaxy>, timeout=5)
if (result != None):
	client.publish(loc_ana, 'home', retain=True)
else:
	client.publish(loc_ana, 'not_home', retain=True)


client.disconnect()
