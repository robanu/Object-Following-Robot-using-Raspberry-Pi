import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 33    #Left ultrasonic sensor
GPIO_ECHO = 35
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      
GPIO.output(GPIO_TRIGGER, False)
while(True):
    start=0
    stop=0
     
    GPIO.output(GPIO_TRIGGER, False)
     
    time.sleep(0.01)
           
     
      
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    begin = time.time()
    while GPIO.input(GPIO_ECHO)==0 and time.time()<begin+0.05:
        start = time.time()
     
    while GPIO.input(GPIO_ECHO)==1 and time.time()<begin+0.1:
        stop = time.time()
    
    elapsed = stop-start
     
    distance = elapsed * 34000
     
      
    distance = distance / 2
     
    print ("Distance : %.1f" % distance)
  
    time.sleep(1)
