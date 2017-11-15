import RPi.GPIO as GPIO
import time
import threading


class ButtonListener:
    """docstring for ButtonListener"""
    def __init__(self, maxDelay=1, mainApp=False):
        super(ButtonListener, self).__init__()
        # variables that Adam uses in his function
        self.Pressed = 0
        self.NotPressed = 1
        self.Button1 = 23
        self.Button2 = 24
        self.Button3 = 25
        # the interval over which to consider a double click
        self.MaxDelay = maxDelay #secs
        # disable double clicks when not in the main app
        self.allowDoubleClick = mainApp
        # this variable will be set to 1-left, 2-up, 3-right, 4-double left, 5-double up, or 6-double right
        self.selection = None
        self.lastTime = None
        self.lastPressed = None
        self.setup_GPIO()

    def setup_GPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
        GPIO.setup(self.Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24
        GPIO.setup(self.Button3, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO25

    def launch(self):
        try:
            threads = []
            buttonNums = [self.Button1, self.Button2, self.Button3]
            for i in range(3):
                t = threading.Thread(target=self.buttonPress, args=(buttonNums[i], ))
                threads.append(t)
                t.start()

        except:
            print("Unable to start thread")
            GPIO.cleanup()

    def buttonPress(self, buttonNum):
    state = NotPressed
    pulseCount = 0
    while True:
        # get input from the GPIO
        newState = GPIO.input(buttonNum)
        # main application or potentially tutorial???
        if self.allowDoubleClick:
            if newState == Pressed and state == NotPressed:
                time.sleep(0.05)
                # two button presses have occurred within the double-click interval
                if(self.lastTime is not None):
                    # potential double click
                    if(self.lastPressed == buttonNum):
                        # valid double press
                        if time.time() < (self.lastTime + MaxDelay):
                            print("Double press", buttonNum)
                            self.lastTime = None
                            self.lastPressed = None
                    # reset last pressed and last time --> this is a correction in a double press
                    else:
                        self.lastTime = time.time()
                        self.lastPressed = buttonNum
                else:
                    self.lastTime = time.time()
                    self.lastPressed = buttonNum
            # no push --> not input to read
            elif newState == NotPressed:
                state = NotPressed
            
            # check if the interval has expired to pick up a single press
            if (self.lastTime is not None 
                and time.time() > (self.lastTime + self.MaxDelay)
                and self.lastPressed == buttonNum):
                    self.lastTime = None
                    print("Single Press", self.lastPressed)
                    self.lastPressed = None
        # no double clicks - register click immediately
        else:
            if newState == Pressed and state == NotPressed:
                print("Single Press", buttonNum)
            elif newState == NotPressed:
                state = NotPressedkb

    def reset(self):
        self.lastPressed = None
        self.lastTime = None

