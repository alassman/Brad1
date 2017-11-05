import tkinter as tk 
from tkinter import *
import UI_code.navigation

# TODO: I MUST PASS IN THE SETTINGS TO DISPLAY THEM CORRECTLY!!!!

class settingsScreen(Frame):
	def __init__(self, parent=None, num_words=3, sleeptime=3, clicktime=1):
		Frame.__init__(self, parent)
		# setting variables
		self.num_words = num_words
		self.clicktime = clicktime
		self.sleeptime = sleeptime
		self.parent = parent
		self.pack()
		
		self.parent.bind("<KeyRelease>", self.on_button_press)

		self.font_size = 40
		self.font_array = [12, 18, 24, 32, 40, 48, 56, 64]
		self.parent.bind("<KeyRelease>", self.on_button_press)
		# titles are below
		self.title = None
		self.font_size_label = None
		self.instructions = None
		# location mapping: 0 - exit, 1 - clicktime, 2 - sleeptime, 3 - number of words
		self.location = 0

		self.form_screen()


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
		self.instructions.place(relx=.4, rely=.2)
		# number of words label
		self.num_words_label = Label(self.parent, 
			text="Number of words for the app to display is: " + str(self.num_words), 
			font=("Times New Roman", 18), fg="black")
		self.num_words_label.place(relx=.4, rely=.4)
		# sleep time label
		self.sleeptime_label = Label(self.parent, 
			text="Number of seconds for the microphone to sleep after listening: " + str(self.sleeptime), 
			font=("Times New Roman", 18), fg="black")
		self.sleeptime_label.place(relx=.4, rely=.5)
		# click time lable
		self.clicktime_label = Label(self.parent, 
			text="Number of seconds to consider the double-click interval: " + str(self.clicktime), 
			font=("Times New Roman", 18), fg="black")
		self.clicktime_label.place(relx=.4, rely=.6)
		# exit label
		self.exit = Label(self.parent, text="Exit", font=("Times New Roman", 18, "bold"), fg="black")
		self.exit.place(relx=.45, rely=.7)




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
					self.num_words_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.num_words)
				
		elif(key == 63235):
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
					self.num_words_label["text"] = "Number of seconds for the microphone to sleep after listening: " + str(self.num_words)




