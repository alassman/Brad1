import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
Pressed = 0
NotPressed = 1
Button1 = 23
Button2 = 24
Button3 = 25
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24
GPIO.setup(Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO25

MaxDelay = 0.5 #secs

def buttonPress( buttonNum):
    time.sleep(0.05)
    state = NotPressed
    lastTime = time.time()
    pulseCount = 0
    while True:
        newState = GPIO.input(buttonNum)
        if newState == Pressed and state == NotPressed:
            pulseCount += 1
            state = Pressed
            lastTime = time.time()
        elif newState == NotPressed:
            state = NotPressed
        if time.time() > (lastTime + MaxDelay):
            if pulseCount == 1:
                print("Single Press", buttonNum)
                #this is where a global value will be set
            elif pulseCount == 2:
                print("Double Press", buttonNum)
                #this is where a global value will be set
            elif pulseCount == 3:
                print("ending thread for ", buttonNum)
                break
            pulseCount = 0
try:
    threads = []
    buttonNums = [Button1, Button2, Button3]
    for i in range(3):
        t = threading.Thread(target=buttonPress, args=(buttonNums[i], ))
        threads.append(t)
        t.start()

except:
    print("Unable to start thread")
    GPIO.cleanup()
