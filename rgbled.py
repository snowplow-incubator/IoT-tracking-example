# importing device modules
from machine import Pin, PWM
import time
import dht11

    # device initialisation
# RGB LED 
redpin = PWM(Pin(13))
greenpin = PWM(Pin(12))
bluepin = PWM(Pin(11))

freq_num = 10000
redpin.freq(freq_num)
greenpin.freq(freq_num)
bluepin.freq(freq_num)

# temp and humidity sensor
temperature = 0
humidity = 0
dht = dht11.DHT11(15)
time.sleep(1)

# buttons
redbutton = Pin(7, Pin.IN, Pin.PULL_UP)
yellowbutton = Pin(8, Pin.IN, Pin.PULL_UP)
greenbutton = Pin(9, Pin.IN, Pin.PULL_UP)

def setRed():
    redpin.duty_u16(0)
    greenpin.duty_u16(65535)
    bluepin.duty_u16(65535)

def setGreen():
    redpin.duty_u16(65535)
    greenpin.duty_u16(0)
    bluepin.duty_u16(65535)
    
def setYellow():
    redpin.duty_u16(0)
    greenpin.duty_u16(0)
    bluepin.duty_u16(65535)
    
def setOff():
    redpin.duty_u16(65535)
    greenpin.duty_u16(65535)
    bluepin.duty_u16(65535)

def redButtonClick():
    setRed()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)
    setRed()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)
    setRed()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)

def yellowButtonClick():
    setYellow()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)
    setYellow()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)
    setYellow()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)

def greenButtonClick():
    setGreen()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)
    setGreen()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)
    setGreen()
    time.sleep(0.5)
    setOff()
    time.sleep(0.5)

def sensorRead():
    # temp and humidity sensor - DHT11 sensor
    if dht.measure() == 0:
        print("DHT data error")
        return
    temperature = dht.temperature()
    humidity = dht.humidity()
    print("temperature: %0.2fC  humidity: %0.2f"%(temperature, humidity) + "%")
    

while True:
    setOff()
    
    if not redbutton.value():
        sensorRead()
        redButtonClick()
        
    elif not yellowbutton.value():
        sensorRead()
        yellowButtonClick()
        
    elif not greenbutton.value():
        sensorRead()
        greenButtonClick()
        