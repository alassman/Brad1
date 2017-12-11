from itertools import cycle
import tkinter as tk 
import os, sys
from tkinter import *
import UI_code.navigation
#import threadedDoublePress

class tutorialScreen(tk.Frame):
	def __init__(self, parent, controller, num_words=3, sleeptime=3, clicktime=1):
		tk.Frame.__init__(self, parent)
		#self = parent
		#self.pack()
		self.form_screen()
		#self.bind("<KeyRelease>", self.on_button_press)

		# set up the slideshow
		self.slideshow_counter = None

		# required for carrying the settings
		# self.num_words = num_words
		# self.sleeptime = sleeptime
		# self.clicktime = clicktime

		self.last_key = None
		self.key = None
		self.screen = False

		# start button listener
		#controller.buttonListener = ButtonListener(self.clicktime)
		#controller.buttonListener.launch()
		#_thread.start_new_thread(self.wait_on_button_signal, ())

	def wait_on_button_signal(self, controller):
		self.slideshow(controller)
		controller.buttonListener.startListening(controller.clicktime)
		while self.screen:
			# if there is a selection
			# 1 = left
			# 2 = up
			# 3 = right
			# 4 = double left
			# 5 = double up
			# 6 = double right

			if controller.buttonListener.selection:
				print(controller.buttonListener.selection)
				if (self.slideshow_counter == 0 or self.slideshow_counter == 4 
					or self.slideshow_counter == 5 or self.slideshow_counter == 8
					or self.slideshow_counter == 9):
					self.slideshow_counter += 1
					self.slideshow(controller)
				elif (self.slideshow_counter == 1 and controller.buttonListener.selection == 2):
					print("Here")
					self.slideshow_counter += 1
					self.slideshow(controller)
				elif self.slideshow_counter == 2 and controller.buttonListener.selection == 3:
					self.slideshow_counter += 1
					self.slideshow(controller)
				elif self.slideshow_counter == 3 and controller.buttonListener.selection == 1:
					self.slideshow_counter += 1
					self.slideshow(controller)
				elif self.slideshow_counter == 6:
					if controller.buttonListener.selection > 3 and controller.buttonListener.selection < 7:
						self.slideshow_counter += 1
						self.slideshow(controller)
				elif self.slideshow_counter == 7:
					if controller.buttonListener.selection >= 4:
						self.slideshow_counter += 1
						self.slideshow(controller)
				elif self.slideshow_counter == 10:
					# UI_code.navigation.back_to_menu(self, False, self.num_words, 
					# 	self.sleeptime, self.clicktime)
					controller.buttonListener.finishListening()
					controller.show_frame("MainMenu")
					#return
				controller.buttonListener.finishListening()

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
		title = Label(self, text="Tutorial", font=("Times New Roman", 40), fg="black", bg="white")
		title.pack(fill=X, side=TOP)
		#title.place(x=400, y=50, anchor="center")

		#text = "FOR THIS ALPHA VERSION,\nNAVIGATE THE MAIN\nAPPLICATION PAGE USING THE ARROW KEYS\nPRESS ANY KEY TO GO BACK TO THE MAIN MENU"
		#instructions = Label(self, text= text, font=("Times New Roman", 48), fg="black")
		#instructions.place(relx=.05, rely=.4)

	def slideshow(self, controller):
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
			self.picture_display.pack(side=BOTTOM, anchor=CENTER)
		self.picture = tk.PhotoImage(file=self.image_files[self.slideshow_counter])
		self.picture_display.config(image=self.picture)
		# Have to restart listening for next slide
		controller.buttonListener.startListening(controller.clicktime)


	# # navigate back to the menu screen
	# def on_button_press(self, event):
	# 	self.key = int(ord(event.char))
	# 	if (self.slideshow_counter == 0 or self.slideshow_counter == 4 
	# 		or self.slideshow_counter == 5 or self.slideshow_counter == 8
	# 		or self.slideshow_counter == 9):
	# 		self.slideshow_counter += 1
	# 		self.slideshow()
	# 	elif (self.slideshow_counter == 1 and self.key == 63232):
	# 		print("Here")
	# 		self.slideshow_counter += 1
	# 		self.slideshow()
	# 	elif self.slideshow_counter == 2 and int(self.key) == 63235:
	# 		self.slideshow_counter += 1
	# 		self.slideshow()
	# 	elif self.slideshow_counter == 3 and self.key == 63234:
	# 		self.slideshow_counter += 1
	# 		self.slideshow()
	# 	elif self.slideshow_counter == 6:
	# 		if self.key == self.last_key:
	# 			self.last_key = None
	# 			self.slideshow_counter += 1
	# 			self.slideshow()
	# 		else:
	# 			self.last_key = self.key
	# 	elif self.slideshow_counter == 7:
	# 		if self.key == 63234 and self.last_key == 63234:
	# 			self.last_key = None
	# 			self.slideshow_counter += 1
	# 			self.slideshow()
	# 		else:
	# 			self.last_key = self.key
	# 	elif self.slideshow_counter == 10:
	# 		UI_code.navigation.back_to_menu(self, False, self.num_words, 
	# 			self.sleeptime, self.clicktime)
