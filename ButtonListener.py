import RPi.GPIO as GPIO
import time
import threading


class ButtonListener:
    """This class allows for single and double presses to be read from custom foot pedal"""
    def __init__(self, mainApp=False):
        super(ButtonListener, self).__init__()
        # variables that Adam uses in his function
        self.Pressed = 0
        self.NotPressed = 1
        self.left = 23
        self.up = 24
        self.right = 25
        self.leftListen = False
        self.upListen = False
        self.rightListen = False

        # the interval over which to consider a double click
        # disable double clicks when not in the main app
        self.allowDoubleClick = mainApp
        # this variable will be set to 1-left, 2-up, 3-right, 4-double left, 5-double up, or 6-double right
        self.selection = None
        self.tempSelection = None
        self.startTime = time.time()
        self.listening = False
        self.clicktime = 0.5
        self.setup_GPIO()

    def setup_GPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
        GPIO.setup(self.up, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24
        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO25
        GPIO.add_event_detect(self.left, GPIO.FALLING, bouncetime=100)  # add rising edge detection on a channel
        GPIO.add_event_detect(self.up, GPIO.FALLING, bouncetime=100)  # add rising edge detection on a channel
        GPIO.add_event_detect(self.right, GPIO.FALLING, bouncetime=100)  # add rising edge detection on a channel
        
    def launch(self):
        try:
            threads = []
            buttonNums = [self.left, self.up, self.right]
            for i in range(3):
                t = threading.Thread(target=self.waitingToListen, args=(buttonNums[i], ))
                threads.append(t)
                t.start()

        except:
            print("Unable to start thread")
            GPIO.cleanup()

    def startListening(self, clicktime=0.5):
        self.clicktime = clicktime
        self.listening = True

    def finishListening(self):
        self.selection = None
        self.tempSelection = None
        
    def waitingToListen(self, buttonNum):
        while(True):
            if self.listening:
                self.resetEventListenerQueue(buttonNum)
                self.buttonPress(buttonNum)
                self.listening = False

    # Function returns 'clicktime' seconds after first button is hit if no other button is hit.
    # Function returns immediatly if second button is hit and matches the first button hit
    # If a second button is hit that does not match the first, startTime is reset
    # Selected button is set in 'self.selection' variable
    def buttonPress(self, buttonNum):
        self.startTime = time.time() + 15 # give Brad 15 seconds to make any selection
        while True:
            if (time.time() > (self.startTime + self.clicktime)) and self.tempSelection != None:
                self.selection = self.tempSelection
                print("Single click SET: ", buttonNum)
                break
            if GPIO.event_detected(buttonNum):
                time.sleep(0.01) # debounce for 1mSec
                if GPIO.input(buttonNum) == self.Pressed:
                    # Push is registered
                    if self.tempSelection == None:
                        # First click
                        print("First click on: ", buttonNum)
                        self.startTime = time.time()
                        self.tempSelection = buttonNum - 22
                    elif self.tempSelection == (buttonNum - 22):
                        # Second click
                        print("Double click on: ", buttonNum)
                        self.tempSelection = self.tempSelection + 3
                        self.selection = self.tempSelection
                        break
                    else:
                        # Correction click
                        self.tempSelection = buttonNum - 22
                        self.startTime = time.time()


                        
    def resetEventListenerQueue(self, buttonNum):
        GPIO.remove_event_detect(buttonNum)
        time.sleep(0.025)
        GPIO.add_event_detect(buttonNum, GPIO.FALLING, bouncetime=50)  # add rising edge detection on a channel


