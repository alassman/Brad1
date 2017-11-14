from itertools import cycle
import tkinter as tk 
from tkinter import *
import UI_code.navigation

class tutorialScreen(Frame):
	def __init__(self, parent=None, num_words=3, sleeptime=3, clicktime=1):
		Frame.__init__(self, parent)
		self.parent = parent
		self.pack()
		self.form_screen()
		self.parent.bind("<KeyRelease>", self.on_button_press)

		# set up the slideshow
		self.slideshow_counter = None
		self.slideshow()

		# required for carrying the settings
		self.num_words = num_words
		self.sleeptime = sleeptime
		self.clicktime = clicktime

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
			self.image_files = [
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/first_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/second_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/third_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/fourth_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/fifth_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/sixth_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/seventh_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/eigth_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/ninth_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/tenth_slide.gif',
				'/Users/roblevy/Desktop/Brad1/UI_code/tutorial_images/eleventh_slide.gif',
				]
			self.slideshow_counter = 0
			self.picture_display = tk.Label(self)
			self.picture_display.pack(pady=57, anchor=CENTER)
		self.picture = tk.PhotoImage(file=self.image_files[self.slideshow_counter])
		self.picture_display.config(image=self.picture)

	# navigate back to the menu screen
	def on_button_press(self, event):
		if self.slideshow_counter < (len(self.image_files) - 1):
			self.slideshow_counter += 1
			self.slideshow()
		else:
			UI_code.navigation.back_to_menu(self.parent, False, self.num_words, 
				self.sleeptime, self.clicktime)

