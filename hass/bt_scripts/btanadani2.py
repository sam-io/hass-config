import bluetooth
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


broker = '192.168.1.5'
loc_dani = 'hass/dani/localizacion'
loc_ana = 'hass/ana/localizacion'
delay = 300
mac_dani = <mac_iphone>
mac_ana = <mac_galaxy>
client = mqtt.Client("hass-client")
client.connect(broker)
client.loop_start()

while True:
	result = bluetooth.lookup_name(mac_dani, timeout=3)
	if (result != None):
		client.publish(loc_dani, 'home', retain=True)
	else:
		client.publish(loc_dani, 'not_home', retain=True)
	result = bluetooth.lookup_name(mac_ana, timeout=3)
	if (result != None):
		client.publish(loc_ana, 'home', retain=True)
	else:
		client.publish(loc_ana, 'not_home', retain=True)
	time.sleep(delay)
client.disconnect()
