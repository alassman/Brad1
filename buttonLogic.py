import time
import threading 


class buttonLogic:
	def __init__(self):
		self.curButton = 0
		self.lastTime = 0
		self.numPress = 0
		self.conditon = threading.Condition()

	def button(self, channel):
		global doublePressTime
		self.conditon.acquire()
		self.curButton = channel
		self.numPress++
		self.conditon.wait(doublePressTime)

		self.conditon.acquire()
		if self.curButton == channel && self.numPress == 2:
			resetButtons()
			self.conditon.release()
			buttonPressed(channel, true)
			
		elif self.curButton == channel
			resetButtons()
			self.conditon.release()
			buttonPressed(channel, false)

		else 
			self.curButton = channel
			self.numPress = 0

	def leftButton(self):
		button(Left)
			
	def rightButton(self):
		button(Right)

	def upButton(self):
		button(Up)
		
	def resetButtons(self):
		self.curButton = 0
		self.numPress = 0




