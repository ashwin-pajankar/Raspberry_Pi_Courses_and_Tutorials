import Adafruit_DHT as dht    		# Importing Adafruit library for DHT22
from time import sleep           	# Impoting sleep from time library to add delay

try:
    while 1:                		# Loop will run forever
        print("Reading Data...")
        humi, temp = dht.read_retry(dht.DHT22, 23)
        print("Temperature {0:0.1f} *C, Humidity {1:0.1f}".format(temp, humi))
	# Reading humidity and temperature
        sleep(3)

# If keyboard Interrupt is pressed
except KeyboardInterrupt:
    pass  				# Go to next line
