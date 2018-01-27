
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

from picamera import PiCamera
from time import sleep
from datetime import datetime

timestamp = datetime.now().isoformat()
photo_path = '/home/pi/Python, Camera/image captures/%s.jpg' %timestamp


while True:  									# this creates an infinite loop, which will instruct the 												processor to constantly check the pin state
        input_value = GPIO.input(12)
        if input_value == False: 						# this has been made for a switch with a pull-up resistor i.e. 												it's default state is high and pressing the button will 											pull-low
            camera=PiCamera()

            camera.rotation = 180
            camera.start_preview()
            sleep(3)
            camera.capture(photo_path)
            camera.stop_preview()
            while input_value == False:  					#  this is an embedded loop which stops python printing the 												message every clock cycle.   
                input_value = GPIO.input (12)  					# Instead it gets python to just check the status of the pin and 												assign it to the variable 'input_variable'.
                                               					# When the button is released, the variable value is 'True' and 											the loop is terminated.
