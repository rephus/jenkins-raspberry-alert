
import requests
import time
import settings 
import datetime

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(settings.relay_pin, GPIO.OUT)


def log(msg):
    print ("[{}] {}".format(datetime.datetime.now(), msg))


def active_alarm(): 
    try:
        log("Activating alarm")
        GPIO.output(settings.relay_pin, GPIO.LOW)        
        time.sleep(settings.time_active)
        log("Deactivating alarm")
        GPIO.output(settings.relay_pin, GPIO.HIGH) 
        time.sleep(settings.frequency) # Sleep 1 hour
    except Exception as e:
        print("Unable to run active_alarm method", e)

while True:
    try: 
        log("Making request to " + settings.url)
        response = requests.get(settings.url, json=[], headers=settings.headers)
        #print ("Response ", response)
        for job in response.json()['jobs']:
            if 'safety check' in job['name'].lower():
                log ("Jenkins task {}: {}".format(job['name'], job['color']))
                if 'red' in job['color']: 
                    active_alarm()
                    break

    except Exception as e: 
        print("ERROR: Unable to make request to "+ settings.url, e)
        
    
    time.sleep(60) 


