from itertools import cycle
import tkinter as tk 
import os, sys
from tkinter import *
import UI_code.navigation
#import threadedDoublePress

class tutorialScreen(Frame):
	def __init__(self, parent=None, num_words=3, sleeptime=3, clicktime=1):
		Frame.__init__(self, parent)
		self.parent = parent
		self.pack()
		self.form_screen()
		#self.parent.bind("<KeyRelease>", self.on_button_press)

		# set up the slideshow
		self.slideshow_counter = None
		self.slideshow()

		# required for carrying the settings
		self.num_words = num_words
		self.sleeptime = sleeptime
		self.clicktime = clicktime

		self.last_key = None
		self.key = None
		# start button listener
		self.buttonListener = ButtonListener(self.clicktime)
		self.buttonListener.launch()
		_thread.start_new_thread(self.wait_on_button_signal, ())

	def wait_on_button_signal():
		while True:
			# if there is a selection
			# 1 = left
			# 2 = up
			# 3 = right
			# 4 = double left
			# 5 = double up
			# 6 = double right

			if self.buttonListener.selection:
				if (self.slideshow_counter == 0 or self.slideshow_counter == 4 
					or self.slideshow_counter == 5 or self.slideshow_counter == 8
					or self.slideshow_counter == 9):
					self.slideshow_counter += 1
					self.slideshow()
				elif (self.slideshow_counter == 1 and self.button.selection == 2):
					print("Here")
					self.slideshow_counter += 1
					self.slideshow()
				elif self.slideshow_counter == 2 and self.button.selection == 3:
					self.slideshow_counter += 1
					self.slideshow()
				elif self.slideshow_counter == 3 and self.button.selection == 1:
					self.slideshow_counter += 1
					self.slideshow()
				elif self.slideshow_counter == 6:
					if self.button.selection > 3 and self.button.selection < 7:
						self.slideshow_counter += 1
						self.slideshow()
				elif self.slideshow_counter == 7:
					if self.buttonListener.selection == 4:
						self.slideshow_counter += 1
						self.slideshow()
				elif self.slideshow_counter == 10:
					UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
						self.sleeptime, self.clicktime)
			# this will ensure that the selected word is only spoken once
			self.buttonListener.selection = None

	def form_screen(self):
    	# set color to off-white
		self.configure(background="#FEFEFA")
    	# set title of screen to none
		self.winfo_toplevel().title("")
		# set titles
		self.load_titles()
		# load arrows
		#self.load_arrows()

	def load_titles(self):
		title = Label(self.parent, text="Tutorial", font=("Times New Roman", 60), fg="black")
		#title.pack(fill=X, side=TOP, anchor=W)
		title.place(relx=.38, rely=0)
		#text = "FOR THIS ALPHA VERSION,\nNAVIGATE THE MAIN\nAPPLICATION PAGE USING THE ARROW KEYS\nPRESS ANY KEY TO GO BACK TO THE MAIN MENU"
		#instructions = Label(self.parent, text= text, font=("Times New Roman", 48), fg="black")
		#instructions.place(relx=.05, rely=.4)

	def slideshow(self):
		# set up the slideshow variables
		if self.slideshow_counter is None:
			print(os.getcwd())
			self.image_files = [
				os.getcwd() + '/UI_code/tutorial_images/first_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/second_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/third_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/fourth_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/fifth_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/sixth_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/seventh_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/eigth_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/ninth_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/tenth_slide.gif',
				os.getcwd() + '/UI_code/tutorial_images/eleventh_slide.gif',
				]
			self.slideshow_counter = 0
			self.picture_display = tk.Label(self)
			self.picture_display.pack(pady=57, anchor=CENTER)
		self.picture = tk.PhotoImage(file=self.image_files[self.slideshow_counter])
		self.picture_display.config(image=self.picture)

	# navigate back to the menu screen
	def on_button_press(self, event):
		self.key = int(ord(event.char))
		if (self.slideshow_counter == 0 or self.slideshow_counter == 4 
			or self.slideshow_counter == 5 or self.slideshow_counter == 8
			or self.slideshow_counter == 9):
			self.slideshow_counter += 1
			self.slideshow()
		elif (self.slideshow_counter == 1 and self.key == 63232):
			print("Here")
			self.slideshow_counter += 1
			self.slideshow()
		elif self.slideshow_counter == 2 and int(self.key) == 63235:
			self.slideshow_counter += 1
			self.slideshow()
		elif self.slideshow_counter == 3 and self.key == 63234:
			self.slideshow_counter += 1
			self.slideshow()
		elif self.slideshow_counter == 6:
			if self.key == self.last_key:
				self.last_key = None
				self.slideshow_counter += 1
				self.slideshow()
			else:
				self.last_key = self.key
		elif self.slideshow_counter == 7:
			if self.key == 63234 and self.last_key == 63234:
				self.last_key = None
				self.slideshow_counter += 1
				self.slideshow()
			else:
				self.last_key = self.key
		elif self.slideshow_counter == 10:
			UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
				self.sleeptime, self.clicktime)
