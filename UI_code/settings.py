import tkinter as tk 
from tkinter import *
import UI_code.navigation

# TODO: I MUST PASS IN THE SETTINGS TO DISPLAY THEM CORRECTLY!!!!

class settingsScreen(Frame):
	def __init__(self, parent=None, num_words, clicktime, sleeptime):
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
		text = "Press the up key to exit.\nLeft to lessen font size.\nRight to raise font size."
		self.instructions = Label(self.parent, text= text, font=("Times New Roman", self.font_size), fg="black")
		self.instructions.place(relx=.25, rely=.5)
		self.font_size_label = Label(self.parent, text="Font size is: " + str(self.font_size), fg="black")
		self.font_size_label.place(relx=.25, rely=.2)



	# navigate back to the menu screen
	def on_button_press(self, event):
		key = ord(event.char)
		if(key == 63232):
			UI_code.navigation.back_to_menu(self.parent)
		elif(key == 63234):
			index = self.font_array.index(self.font_size) - 1
			if index > -1:
				self.font_size = self.font_array[index]
		elif(key == 632345):
			if index < len(self.font_array):
				index = self.font_array.index(self.font_size) + 1
				self.font_size = self.font_array[index]
		self.instructions["font"] = ("Time New Roman", self.font_size)
		self.font_size_label["font"] = ("Time New Roman", self.font_size)
		self.font_size_label["text"] = "Font size is: " + str(self.font_size)
		self.title["font"] = ("Time New Roman", self.font_size)



