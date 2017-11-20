import tkinter as tk 
import _thread, time, os
import subprocess
import sys

import UI_code.navigation
from tkinter import *
from speechToText.speak import listen
import tellnext_changed.tellnext.tool as tellnext
import tellnext_changed.tellnext.model as tellnext_model
import tellnext_changed.tellnext.store as store
#import threadedDoublePress

# from mastodon.bindict import BinaryDictionary

# CHANGE TO LIHU'S CODE: I WILL ONLY NEED TO CALL next_word() FROM tellnext_changed.tellnext.tool

class applicationScreen(Frame):
	def __init__(self, parent=None, num_words=3, mic_sleep=3, clicktime=1):
		print("Thread id in init(): " + str(_thread.get_ident()))
		Frame.__init__(self, parent)
		# THE FOLLOWING VARIABLES COME FROM SETTINGS
		self.num_words = num_words
		self.sleeptime = mic_sleep
		self.clicktime = clicktime
		# THE FOLLOWING ARE NECESSARY FOR THIS APP TO FUNCTION
		self.parent = parent
		self.first_word = None
		self.second_word = None
		self.third_word = None
		self.fourth_word = None
		self.fifth_word = None
		self.selected_word = None
		self.selected_word_label = None
		self.last_spoken = []
		_thread.start_new_thread(self.listen_for_words, ())
		self.pack()
		self.form_screen()
		# launch the button listener
		#self.buttonListener = ButtonListener(self.clicktime, True)
		#self.buttonListener.launch()
		#_thread.start_new_thread(self.wait_on_button_signal, ())
		# ALPHA CODE ONLY
		self.first_key = None
		self.second_key = None
		self.end_time = None
		self.quit = False
		self.last_two_words = [None, None]

		self.parent.bind("<KeyRelease>", self.on_button_press)
		_thread.start_new_thread(self.wait_on_button_press, ())

	def wait_on_button_signal():
		while self.quit is not True:
			# if there is a selection
			if self.buttonListener.selection:
				# set the selected word
				if self.buttonListener.selection == 1:
					print("SINGLE PRESS LEFT")
					self.selected_word = self.first_word["text"]
				elif self.buttonListener.selection == 2:
					print("SINGLE PRESS UP")
					self.selected_word = self.second_word["text"]
				elif self.buttonListener.selection == 3:
					print("SINGLE PRESS RIGHT")
					self.selected_word = self.third_word["text"]
				elif self.buttonListener.selection == 4:
					print("DOUBLE PRESS LEFT")
					UI_code.navigation.back_to_menu(self.parent, True, 
						self.num_words, self.sleeptime, self.clicktime)
					self.quit = True
				elif self.buttonListener.selection == 5:
					print("DOUBLE PRESS UP")
					self.selected_word = self.fourth_word["text"]
				else:
					print("DOUBLE PRESS RIGHT")
					self.selected_word = self.fifth_word["text"]

				# display the word
				self.selected_word_label["text"] = self.selected_word
				# say the word
				subprocess.call('say ' + self.selected_word, shell=True)
				tellnext.update_model(self.last_two_words[0], self.last_two_words[1], self.selected_word)
			# this will ensure that the selected word is only spoken once
			self.buttonListener.selection = None


	def listen_for_words(self):
		print("listening for words")
		words_list = []
		while self.quit is not True:
			# sleep for 5 seconds before listening again
			time.sleep(self.sleeptime)
			# no word on screen was selected
			if self.selected_word is None:
				print("no selected word")
				# call Jenny's function to hear from microphone
				words_from_mic = listen()
				# parse words from Jenny's function
				words_list = words_from_mic.split()
				if(len(words_list) > 2):
					words_list = words_list[len(words_list) - 2:]
				elif(len(words_list) == 1):
					words_list.append(None) 
				# call Lihu's function
				word_predictions = tellnext.new_next_word(words_list[0], words_list[1])
				print(word_predictions)
				self.last_two_words[0] = words_list[0]
				self.last_two_words[1] = words_list[1]
			# predict word from selected word on screen
			else:
				# append to words_list
				words_list.append(self.selected_word)
				if(len(words_list) >= 2):
					words_list = words_list[len(words_list) - 2:]
				elif len(words_list) == 1:
					words_list.append(None)
				# call Lihu's function
				
				word_predictions = tellnext.new_next_word(words_list[0], words_list[1])
				print(word_predictions)
				self.last_two_words[0] = words_list[0]
				self.last_two_words[1] = words_list[1]
				# set the selected word to None
				self.selected_word = None
			print("length of word predictions: " +str(len(word_predictions)))
			self.last_spoken = words_list
			# update the labels --> THIS NEEDS TO USE LIHU's PREDICTION
			self.first_word["text"] = word_predictions[0]
			self.second_word["text"] = word_predictions[1]
			self.third_word["text"] = word_predictions[2]
			if self.num_words > 3:
				self.fourth_word["text"] = word_predictions[3]
			if self.num_words > 4:
				self.fifth_word["text"] = word_predictions[4]
			#words_list = []

	# this function is alpha only
	def on_button_press(self, event):
		if self.first_key is None:
			print("FIRST KEY")
			#first_key = sys.stdin.read(1)
			#first_key = ord( first_key )
			self.first_key = ord(event.char)
			self.end_time = time.time() + self.clicktime
			print("You pressed " + str(self.first_key))
		else:
			print("SECOND KEY")
			if time.time() < self.end_time:
				self.second_key = ord(event.char)
				print("You pressed " + str(self.second_key))
			else:
				self.first_key = ord(event.char)
				self.end_time = time.time() + self.clicktime
				print("You pressed " + str(self.first_key) + "after time expired")
	
	# this function is alpha only		
	def wait_on_button_press(self):
		print("waiting on button press")
		#'''engine = pyttsx.init()
		#engine.say("HELLO WORLD I AM INITIALIZED, MY NAME IS ALFRED")
		#engine.runAndWait()'''
		#text = "HELLO WORLD I AM INITIALIZED, MY NAME IS ALFRED"
		#subprocess.call('say ' + text, shell=True)
		toSay = None
		while not self.quit:
			if self.end_time is not None:
				# this is terrible, but keyboard interrupts are so terrible in this
				while time.time() < self.end_time:
					pass
				# only 1 key pressed
				if self.second_key is None:
					# left press
					if(self.first_key == 63234):
						print("SINGLE LEFT PRESS")
						self.selected_word = self.first_word["text"]
						toSay = self.selected_word
					# up press
					elif(self.first_key == 63232):
						print("SINGLE UP PRESS")
						self.selected_word = self.second_word["text"]
						toSay = self.selected_word
					# down press
					elif(self.first_key == 63235):
						print("SINGLE RIGHT PRESS")
						self.selected_word = self.third_word["text"]
						toSay = self.selected_word
					else:
						self.selected_word = None
						toSay = self.selected_word
					self.first_key = None
					self.end_time = None
				# double click
				elif self.first_key == self.second_key:
					# left press
					if(self.first_key == 63234):
						print("DOUBLE LEFT PRESS")
						# WE NEED TO RESOLVE GOING BACK!!! CIRCULAR DEPENDENCIES
						UI_code.navigation.back_to_menu(self.parent, True, 
							self.num_words, self.sleeptime, self.clicktime)
						self.quit = True
					# up press
					elif(self.fourth_word["text"] and self.first_key == 63232):
						print("DOUBLE UP PRESS")
						self.selected_word = self.fourth_word["text"]
						toSay = self.selected_word
					# down press
					elif(self.fifth_word["text"] and self.first_key == 63235):
						print("DOUBLE RIGHT PRESS")
						self.selected_word = self.fifth_word["text"]
						toSay = self.selected_word
					else:
						self.selected_word = None
						toSay = self.selected_word
					self.first_key = None
					self.second_key = None
					self.end_time = None
				# assume first key press was a mistake, second key becomes first
				# key and second key is reset to nothing
				else:
					self.end_time = time.time()
					self.first_key = self.second_key
					self.second_key = None

				if toSay is not None:
					# display the word
					self.selected_word_label["text"] = toSay
					# say the word
					subprocess.call('say ' + toSay, shell=True)
					




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
		self.load_arrows()
		# load legend
		self.load_legend()


	def load_titles(self):
		# get word predictions
		#word_predictions = tellnext.new_next_word(None, None)
		word_predictions = ["I", "How", "Hello",  "My", "Can"]
		self.first_word = word_predictions[0]
		self.second_word = word_predictions[1]
		self.third_word = word_predictions[2]
		if self.num_words > 3:
			self.fourth_word = word_predictions[3]
		if self.num_words > 4:
			self.fifth_word = word_predictions[4]
		# load titles
		title = Label(self.parent, text="The Microphone is Listening", font=("Times New Roman", 60), fg="black")
		title.pack(fill=X)
		# back button - always there
		back_button = Label(self.parent, text="Back", 
			font=("Times New Roman", 48), fg="black", bg="#ff8080", width=10)
		back_button.place(relx=0.05, rely=0.54, height=55)
		# first word
		self.first_word = Label(self.parent, text=self.first_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		self.first_word.place(relx=0.05, rely=0.44, height=55)
		# second word
		self.second_word = Label(self.parent, text=self.second_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		self.second_word.place(rely=.17, relx=.365, height=55)
		# third word
		self.third_word = Label(self.parent, text=self.third_word , 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		self.third_word.place(rely=0.44, relx=.675, height=55)
		# fourth word
		self.fourth_word = Label(self.parent, text=self.fourth_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		self.fourth_word.place(rely=.27, relx=.365, height=55)
		# fifth word
		self.fifth_word = Label(self.parent, text=self.fifth_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		self.fifth_word.place(rely=0.54, relx=.675, height=55)
		# last selected word
		self.selected_word_label = Label(self.parent, text="", 
			font=("Times New Roman", 48), fg="black", width=10, borderwidth=1,
			relief="solid")
		self.selected_word_label.place(rely=.7, relx=.6)
		temp_label = Label(self.parent, text="Selected Word ^^^", 
			font=("Times New Roman", 36), fg="black", width=15)
		temp_label.place(rely=.83, relx=.58)

	def load_legend(self):
		legend_text = """
------------------------
|   Single Click = Blue   |
|  Double Click = Red   |
------------------------"""
		legend_frame = LabelFrame(self.parent,text='Legend',padx=0, pady=5, 
			foreground="black", font=("Times New Roman", 24))
		legend_frame.place(relx=.1, rely=.67)
		legend_label = Label(legend_frame,text=legend_text, fg="black",
			font=("Times New Roman", 24))
		legend_label.pack()

	def load_arrows(self):
		# arrow left
		canvas_left = Canvas(self.parent, width=55, height=20)
		canvas_left.place(relx=.38, rely=.525)
		left = canvas_left.create_line(5, 10, 55, 10, 
			arrow=tk.FIRST, fill="black", width=10)
		# arrow up
		canvas_up = Canvas(self.parent, width=20, height=55)
		canvas_up.place(relx=.5, rely=.4)
		up = canvas_up.create_line(10, 5, 10, 55, 
			arrow=tk.FIRST, fill="black", width=10)
		# arrow right
		canvas_right = Canvas(self.parent, width=55, height=20)
		canvas_right.place(relx=.59 , rely=.525)
		right = canvas_right.create_line(0, 10, 50, 10, 
			arrow=tk.LAST, fill="black", width=10)