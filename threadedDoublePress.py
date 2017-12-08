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
        self.left = 23
        self.up = 24
        self.right = 25
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
        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
        GPIO.setup(self.up, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24
        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO25

    def launch(self):
        try:
            threads = []
            buttonNums = [self.left, self.up, self.right]
            for i in range(3):
                t = threading.Thread(target=self.buttonPress, args=(buttonNums[i], ))
                threads.append(t)
                t.start()

        except:
            print("Unable to start thread")
            GPIO.cleanup()

    def buttonPress(self, buttonNum):
        state = self.NotPressed
        while True:
            # get input from the GPIO
            newState = GPIO.input(buttonNum)
            # main application or potentially tutorial???
            if self.allowDoubleClick:
                if newState == self.Pressed and state == self.NotPressed:
                    # two button presses have occurred within the double-click interval
                    if(self.lastTime is not None):
                        # potential double click (same button)
                        if(self.lastPressed == buttonNum):
                            # valid double press
                            if time.time() < (self.lastTime + MaxDelay):
                                print("Double press", buttonNum)
                                if(buttonNum == self.left):
                                    self.selection = 4
                                elif(buttonNum == self.up):
                                    self.selection  = 5
                                else:
                                    self.selection = 6
                                self.lastTime = None
                                self.lastPressed = None
                        # reset last pressed and last time --> this is a correction in a double press
                        else:
                            self.lastTime = time.time()
                            self.lastPressed = buttonNum
                    # Single push
                    else:
                        self.lastTime = time.time()
                        self.lastPressed = buttonNum
                    # Deals with debouncing
                    time.sleep(0.05)
                # no push --> not input to read
                elif newState == self.NotPressed:
                    state = self.NotPressed
                            # check if the interval has expired to pick up a single press
                if (self.lastTime is not None 
                    and time.time() >= (self.lastTime + self.MaxDelay)
                    and self.lastPressed == buttonNum):
                        print("Single Press", self.lastPressed)
                        if(buttonNum == self.left):
                            self.selection = 1
                        elif(buttonNum == self.up):
                            self.selection  = 2
                        else:
                            self.selection = 3
                        self.lastTime = None
                        self.lastPressed = None
            # no double clicks - register click immediately
            else:
                if newState == self.Pressed and state == self.NotPressed:
                    print("Single Press", buttonNum)
                    if(buttonNum == self.left):
                        self.selection = 1
                    elif(buttonNum == self.up):
                        self.selection  = 2
                    else:
                        self.selection = 3
                    state = self.Pressed
                elif newState == self.NotPressed:
                    state = self.NotPressed

    def reset(self):
        self.lastPressed = None
        self.lastTime = None

