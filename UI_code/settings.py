import tkinter as tk 
from tkinter import *
import UI_code.navigation
#import threadedDoublePress
import _thread

class settingsScreen(Frame):
	def __init__(self, parent=None, num_words=3, sleeptime=3, clicktime=1, exploration=0.5):
		Frame.__init__(self, parent)
		# setting variables
		self.num_words = num_words
		self.clicktime = clicktime
		self.sleeptime = sleeptime
		self.exploration = exploration
		self.parent = parent
		self.pack()
		
		self.font_size = 40
		#self.font_array = [12, 18, 24, 32, 40, 48, 56, 64]
		self.parent.bind("<KeyRelease>", self.on_button_press)
		# titles are below
		self.title = None
		#self.font_size_label = None
		self.instructions = None
		# location mapping: 0 - exit, 1 - clicktime, 2 - sleeptime, 3 - number of words
		self.location = 0

		self.form_screen()

		# launch button listener
		#self.buttonListener = ButtonListener(self.clicktime)
		#self.buttonListener.launch()
		#_thread.start_new_thread(self.wait_on_button_signal, ())

	def wait_on_button_signal():
		while True:
			# if there is a selection
			if self.buttonListener.selection:
				# left button was pressed
				if self.buttonListener.selection == 1:
					print("LEFT")
					if self.location == 0:
						UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
							self.sleeptime, self.clicktime)
					elif self.location == 1:
						if self.clicktime > 1:
							self.clicktime = self.clicktime - 1
							self.clicktime_label["text"] = ("Number of seconds to consider the double-click interval: " + str(self.clicktime))
					elif self.location == 2:
						if self.sleeptime > 1:
							self.sleeptime = self.sleeptime - 1
							self.sleeptime_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.sleeptime)
					else:
						if self.num_words > 3:
							self.num_words = self.num_words - 1
							self.num_words_label["text"] = "Number of words for the app to display is: " + str(self.num_words)
				# up button was pressed
				elif self.buttonListener.selection == 2:
					print("UP")
					if(self.location == 0):
						self.exit["font"] = ("Times New Roman", 18)
						self.clicktime_label["font"] = ("Times New Roman", 18, "bold")
					elif self.location == 1:
						self.clicktime_label["font"] = ("Times New Roman", 18)
						self.sleeptime_label["font"] = ("Times New Roman", 18, "bold")
					elif self.location == 2:
						self.sleeptime_label["font"] = ("Times New Roman", 18)
						self.num_words_label["font"] = ("Times New Roman", 18, "bold")
					else:
						self.num_words_label["font"] = ("Times New Roman", 18)
						self.exit["font"] = ("Times New Roman", 18, "bold")
					self.location = (self.location + 1) % 4
				# right button was pressed
				else:
					print("Right")
					if self.location == 0:
						UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
							self.sleeptime, self.clicktime)
					elif self.location == 1:
						self.clicktime = 1 + self.clicktime
						self.clicktime_label["text"] = ("Number of seconds to consider the double-click interval: " + str(self.clicktime))
					elif self.location == 2:
						self.sleeptime = self.sleeptime + 1
						self.sleeptime_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.sleeptime)
					else:
						if self.num_words < 5:
							self.num_words = self.num_words + 1
							self.num_words_label["text"] = "Number of words for the app to display is: " + str(self.num_words)
			# this will ensure that the selected word is only spoken once
			self.buttonListener.selection = None


	def form_screen(self):
    	# set color to off-white
		self.configure(background="#FEFEFA")
    	# set title of screen to none
		self.winfo_toplevel().title("")
		# cover full screen
		#self.cover_full_screen()
		# set titles
		self.load_titles()
		# load arrows
		#self.load_arrows()

	def load_titles(self):
		self.title = Label(self.parent, text="Settings", font=("Times New Roman", self.font_size), fg="black")
		self.title.pack(fill=X)
		# instruction label
		text = "Press the up key to rotate.\nLeft to lessen variable.\nRight to increase variable value."
		self.instructions = Label(self.parent, text= text, font=("Times New Roman", 18), fg="black")
		self.instructions.place(relx=.35, rely=.2)
		
		# exploration_ratio
		self.exploration_label = Label(self.parent,
			text="Probability that a random word will be returned during prediction: " + str(self.exploration),
			font=("Times New Roman", 18), fg="black")
		self.exploration_label.place(relx=.3, rely=.4)
		# number of words label
		self.num_words_label = Label(self.parent, 
			text="Number of words for the app to display is: " + str(self.num_words), 
			font=("Times New Roman", 18), fg="black")
		self.num_words_label.place(relx=.35, rely=.5)
		# sleep time label
		self.sleeptime_label = Label(self.parent, 
			text="Number of seconds for the microphone to sleep after listening: " + str(self.sleeptime), 
			font=("Times New Roman", 18), fg="black")
		self.sleeptime_label.place(relx=.35, rely=.6)
		# click time lable
		self.clicktime_label = Label(self.parent, 
			text="Number of seconds to consider the double-click interval: " + str(self.clicktime), 
			font=("Times New Roman", 18), fg="black")
		self.clicktime_label.place(relx=.35, rely=.7)
		
		# exit label
		self.exit = Label(self.parent, text="Exit", font=("Times New Roman", 18, "bold"), fg="black")
		self.exit.place(relx=.4, rely=.8)



	# YOU CAN DELETE THIS FUNCTION AFTER YOU HAVE IT WORKING ON RASP. PI
	# navigate back to the menu screen
	def on_button_press(self, event):
		key = ord(event.char)
		if(key == 63232):
			print("UP")
			if(self.location == 0):
				self.exit["font"] = ("Times New Roman", 18)
				self.clicktime_label["font"] = ("Times New Roman", 18, "bold")
			elif self.location == 1:
				self.clicktime_label["font"] = ("Times New Roman", 18)
				self.sleeptime_label["font"] = ("Times New Roman", 18, "bold")
			elif self.location == 2:
				self.sleeptime_label["font"] = ("Times New Roman", 18)
				self.num_words_label["font"] = ("Times New Roman", 18, "bold")
			elif self.location == 3:
				self.num_words_label["font"] = ("Times New Roman", 18)
				self.exploration_label["font"] = ("Times New Roman", 18, "bold")
			else:
				self.exploration_label["font"] = ("Times New Roman", 18)
				self.exit["font"] = ("Times New Roman", 18, "bold")

			self.location = (self.location + 1) % 5
		elif(key == 63234):
			if self.location == 0:
				print("LEFT")
				UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
					self.sleeptime, self.clicktime, self.exploration)
			elif self.location == 1:
				if self.clicktime > 1:
					self.clicktime = self.clicktime - 1
					self.clicktime_label["text"] = ("Number of seconds to consider the double-click interval: " + str(self.clicktime))
			elif self.location == 2:
				if self.sleeptime > 1:
					self.sleeptime = self.sleeptime - 1
					self.sleeptime_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.sleeptime)
			elif self.location == 4:
				if self.exploration > 0:
					self.exploration = self.exploration - 0.1
					self.exploration_label["text"] = "Probability that a random word will be returned during prediction: " + str(self.exploration)
			else:
				if self.num_words > 3:
					self.num_words = self.num_words - 1
					self.num_words_label["text"] = "Number of words for the app to display is: " + str(self.num_words)
				
		elif(key == 63235):
			print("Right")
			if self.location == 0:
				UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
					self.sleeptime, self.clicktime, self.exploration)
			elif self.location == 1:
				self.clicktime = 1 + self.clicktime
				self.clicktime_label["text"] = ("Number of seconds to consider the double-click interval: " + str(self.clicktime))
			elif self.location == 2:
				self.sleeptime = self.sleeptime + 1
				self.sleeptime_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.sleeptime)
			elif self.location == 4:
				if self.exploration < 1:
					self.exploration = self.exploration + 0.1
					self.exploration_label["text"] = "Probability that a random word will be returned during prediction: " + str(self.exploration)
			else:
				if self.num_words < 5:
					self.num_words = self.num_words + 1
					self.num_words_label["text"] = "Number of words for the app to display is: " + str(self.num_words)




