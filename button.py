import time
import threading
import RPi.GPIO as GPIO

class Button:
	global get_button
	def __init__(self):
		self.cur = 0
		#self.numPress = 0
		self.cv = threading.Condition()
		self.map = {}
		self.map[Left] = 0
		self.map[Right] = 0
		self.map[Up] = 0
		#self.threads = []
		print("init")
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(Left, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
		GPIO.setup(Up, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO24
		GPIO.setup(Right, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO25
		GPIO.add_event_detect(Left, GPIO.FALLING, callback=self.get_button, bouncetime=50)
		GPIO.add_event_detect(Up, GPIO.FALLING, callback=self.get_button, bouncetime=50)
		GPIO.add_event_detect(Right, GPIO.FALLING, callback=self.get_button, bouncetime=50)



	def get_button(self, channel):
		print("HERE")
		if map[channel] == 0:
			self.cv.acquire()
			self.cur = channel
			self.cv.release()
			t = threading.Thread(target=self.buttonPress, args=(buttonNums[i], ))
		else:
			self.cv.acquire()
			if channel == self.cur:	
				++self.map[channel] 
				conditon.notifyAll()
			self.cv.release()

	def left_button(self):
		global doublePressTime
		self.cv.acquire()
		self.map[Up] = self.map[Right] = 0
		conditon.wait(doublePressTime)

		if self.cur == Left and self.map[Left] == 2:
			self.cv.release()
			buttonPressed(Left, True)
		elif self.cur == Left and self.map[Left] == 1:
			self.cv.release()
			buttonPressed(Left, False)

	def right_button(self):
		global doublePressTime
		self.cv.acquire()
		self.map[Up] = self.map[Left] = 0
		conditon.wait(doublePressTime)

		if self.cur == Right and self.map[Right] == 2:
			self.cv.release()
			buttonPressed(Right, True)
		elif self.cur == Right and self.map[Right] == 1:
			self.cv.release()
			buttonPressed(Right, False)

	def up_button(self):
		global doublePressTime
		self.cv.acquire()
		self.map[Left] = self.map[Right] = 0
		conditon.wait(doublePressTime)

		if self.cur == Up and self.map[Up] == 2:
			self.cv.release()
			buttonPressed(Up, True)
		elif self.cur == Up and self.map[Up] == 1:
			self.cv.release()
			buttonPressed(Up, False)


