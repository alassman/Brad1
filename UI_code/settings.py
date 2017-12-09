import tkinter as tk 
from tkinter import *
import UI_code.navigation
import threadedDoublePress
import _thread
from threadedDoublePress import ButtonListener


class settingsScreen(tk.Frame):
	def __init__(self, parent, controller, num_words=3, sleeptime=3, clicktime=1):
		tk.Frame.__init__(self, parent)
		# setting variables
		# self = parent
		self.num_words = num_words
		self.clicktime = clicktime
		self.sleeptime = sleeptime
		#self.parent = parent
		#self.pack()
		
		self.font_size = 40
		self.font_array = [12, 18, 24, 32, 40, 48, 56, 64]
		self.form_screen()
		#self.bind("<KeyRelease>", self.on_button_press)
		# titles are below
		self.title = None
		self.font_size_label = None
		self.instructions = None
		# location mapping: 0 - exit, 1 - clicktime, 2 - sleeptime, 3 - number of words
		self.location = 0

	
		# launch button listener
		#self.buttonListener = ButtonListener(self.clicktime)
		#self.buttonListener.launch()
		#_thread.start_new_thread(self.wait_on_button_signal, ())

	def wait_on_button_signal(self):
		while True:
			# if there is a selection
			if self.buttonListener.selection:
				# left button was pressed
				if self.buttonListener.selection == 1:
					print("LEFT")
					if self.location == 0:
						UI_code.navigation.back_to_menu(self, False, self.num_words, 
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
							self.num_words_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.num_words)
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
						UI_code.navigation.back_to_menu(self, False, self.num_words, 
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
							self.num_words_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.num_words)
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
		self.title = Label(self, text="Settings", font=("Times New Roman", 40), fg="black")
		self.title.pack(fill=X)
		# instruction label
		text = "Up to navigate | Left to lessen | Right to increase."
		self.instructions = Label(self, text= text, font=("Times New Roman", 18), fg="black")
		#self.instructions.place(relx=.35, rely=.2)
		self.instructions.place(x=400, y=100, anchor="center")
		# number of words label
		self.num_words_label = Label(self, 
			text="Words for app to display: " + str(self.num_words), 
			font=("Times New Roman", 24), fg="black")
		#self.num_words_label.place(relx=.35, rely=.4)
		self.num_words_label.place(x=400, y=160, anchor="center")

		# sleep time label
		self.sleeptime_label = Label(self, 
			text="Seconds between speaking: " + str(self.sleeptime), 
			font=("Times New Roman", 24), fg="black")
		#self.sleeptime_label.place(relx=.35, rely=.5)
		
		self.sleeptime_label.place(x=400, y=220, anchor="center")

		# click time lable
		self.clicktime_label = Label(self, 
			text="Seconds allowed for double-click: " + str(self.clicktime), 
			font=("Times New Roman", 24), fg="black")
		#self.clicktime_label.place(relx=.35, rely=.6)
		
		self.clicktime_label.place(x=400, y=280, anchor="center")

		# exit label
		self.exit = Label(self, text="Exit", font=("Times New Roman", 20, "bold"), fg="black")
		#self.exit.place(relx=.4, rely=.7)
		self.exit.place(x=400, y=350, anchor="center")




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
			else:
				self.num_words_label["font"] = ("Times New Roman", 18)
				self.exit["font"] = ("Times New Roman", 18, "bold")
			self.location = (self.location + 1) % 4
		elif(key == 63234):
			if self.location == 0:
				print("LEFT")
				UI_code.navigation.back_to_menu(self, False, self.num_words, 
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
					self.num_words_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.num_words)
				
		elif(key == 63235):
			print("Right")
			if self.location == 0:
				UI_code.navigation.back_to_menu(self, False, self.num_words, 
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
					self.num_words_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.num_words)




