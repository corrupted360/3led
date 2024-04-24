import RPI.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
debug_messages = 1
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")
hardware_test_messages = 1
if hardware_test_messages : print("Hardware Test Message are 'ON'")
else : print("Hardware Test Message are 'OFF'")

GPIO.setmode(GPIO.BOARD)

red_LED_pin = 3
GPIO.setup(red_LED_pin,GPIO.OUT)
yellow_LED_pin = 5
GPIO.setup(yellow_LED_pin,GPIO.OUT)
green_LED_pin = 7
GPIO.setup(green_LED_pin,GPIO.OUT)
