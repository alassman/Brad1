import tkinter as tk 
import _thread, time, os
import subprocess
import sys

import UI_code.navigation
from tkinter import *
from speechToText.speak import Listener
import tellnext_changed.tellnext.tool as tellnext
import tellnext_changed.tellnext.model as tellnext_model
import tellnext_changed.tellnext.store as store
#import threadedDoublePress

# from mastodon.bindict import BinaryDictionary

# CHANGE TO LIHU'S CODE: I WILL ONLY NEED TO CALL next_word() FROM tellnext_changed.tellnext.tool

class applicationScreen(tk.Frame):
	def __init__(self, parent, controller):
		print("Thread id in init(): " + str(_thread.get_ident()))
		tk.Frame.__init__(self, parent)
		# THE FOLLOWING VARIABLES COME FROM SETTINGS
		# self.num_words = num_words
		# self.sleeptime = mic_sleep
		# self.clicktime = clicktime
		# THE FOLLOWING ARE NECESSARY FOR THIS APP TO FUNCTION
		#self = parent
		self.first_word = None
		self.second_word = None
		self.third_word = None
		self.fourth_word = None
		self.fifth_word = None
		self.selected_word = None
		self.selected_word_label = None
		self.last_spoken = []
		#self.t1 = _thread.start_new_thread(self.listen_for_words, ())

		# _thread.start_new_thread(self.listen_for_words, ())
		# self.pack()
		self.screen = False
		self.form_screen(controller)
		self.listener = Listener()
		# launch the button listener
		# controller.buttonListener = ButtonListener(self.clicktime, True)
		# controller.buttonListener.launch()
		# _thread.start_new_thread(self.wait_on_button_signal, ())
		# ALPHA CODE ONLY
		self.first_key = None
		self.second_key = None
		self.end_time = None
		self.quit = False
		self.last_two_words = [None, None]


		#self.bind("<KeyRelease>", self.on_button_press)
		#_thread.start_new_thread(self.wait_on_button_press, ())

	def wait_on_button_signal(self, controller):
		#subprocess.call(jack_control start)
		controller.buttonListener.startListening(controller.clicktime)
		while self.screen:
			# if there is a selection
			if controller.buttonListener.selection:
				# set the selected word
				if controller.buttonListener.selection == 1:
					print("SINGLE PRESS LEFT")
					self.selected_word = self.first_word["text"]
				elif controller.buttonListener.selection == 2:
					print("SINGLE PRESS UP")
					self.selected_word = self.second_word["text"]
				elif controller.buttonListener.selection == 3:
					print("SINGLE PRESS RIGHT")
					self.selected_word = self.third_word["text"]
				elif controller.buttonListener.selection == 4:
					print("DOUBLE PRESS LEFT")
					# UI_code.navigation.back_to_menu(self, True, 
					# 	self.num_words, self.sleeptime, self.clicktime)
					# self.quit = True
					controller.buttonListener.finishListening()
					controller.show_frame("MainMenu")
				elif controller.buttonListener.selection == 5:
					print("DOUBLE PRESS UP")
					self.selected_word = self.fourth_word["text"]
				elif controller.buttonListener.selection == 6:
					print("DOUBLE PRESS RIGHT")
					self.selected_word = self.fifth_word["text"]
				else:
					continue
					#should never be here
				controller.buttonListener.finishListening()
				# display the word
				self.selected_word_label["text"] = self.selected_word
				self.selected_word_label["foreground"] = "black"
				# say the word
				subprocess.call('echo ' + self.selected_word +'| festival --tts', shell=True)

				#subprocess.call('say ' + self.selected_word, shell=True)
				tellnext.update_model(self.last_two_words[0], self.last_two_words[1], self.selected_word)
				controller.buttonListener.startListening(controller.clicktime)


	def error_check_listening(self):
		while True:
			if(self.listener.speakAgain is True):
				self.listener.speakAgain = False
				self.selected_word_label["text"] = "Speak Again"
				self.selected_word_label["foreground"] = "red"


	def listen_for_words(self, controller):
		print("listening for words")

		words_list = []

		while self.screen == True:
			# sleep for 5 seconds before listening again
			time.sleep(controller.sleeptime)
			# no word on screen was selected
			if self.selected_word is None:
				print("no selected word")
				# call Jenny's function to hear from microphone
				_thread.start_new_thread(self.error_check_listening, ())
				words_from_mic = self.listener.listen()
				if self.selected_word_label["foreground"] == "red":
					self.selected_word_label["text"] = ""
				# parse words from Jenny's function
				words_list = words_from_mic.split()
				if(len(words_list) > 2):
					words_list = words_list[len(words_list) - 2:]
				elif(len(words_list) == 1):
					words_list.append(None)
				else:
					words_list = [None, None] 
				# call Lihu's function

				word_predictions = tellnext.new_next_word(words_list[0], words_list[1], 
					controller.num_words, controller.exploration)
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
				
				word_predictions = tellnext.new_next_word(words_list[0], words_list[1], 
					controller.num_words, controller.exploration)
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
			if controller.num_words > 3:
				self.fourth_word["text"] = word_predictions[3]
			if controller.num_words > 4:
				self.fifth_word["text"] = word_predictions[4]
			#words_list = []

	# # this function is alpha only
	# def on_button_press(self, event):
	# 	if self.first_key is None:
	# 		print("FIRST KEY")
	# 		#first_key = sys.stdin.read(1)
	# 		#first_key = ord( first_key )
	# 		self.first_key = ord(event.char)
	# 		self.end_time = time.time() + self.clicktime
	# 		print("You pressed " + str(self.first_key))
	# 	else:
	# 		print("SECOND KEY")
	# 		if time.time() < self.end_time:
	# 			self.second_key = ord(event.char)
	# 			print("You pressed " + str(self.second_key))
	# 		else:
	# 			self.first_key = ord(event.char)
	# 			self.end_time = time.time() + self.clicktime
	# 			print("You pressed " + str(self.first_key) + "after time expired")
	
	# # this function is alpha only		
	# def wait_on_button_press(self):
	# 	print("waiting on button press")
	# 	#'''engine = pyttsx.init()
	# 	#engine.say("HELLO WORLD I AM INITIALIZED, MY NAME IS ALFRED")
	# 	#engine.runAndWait()'''
	# 	#text = "HELLO WORLD I AM INITIALIZED, MY NAME IS ALFRED"
	# 	#subprocess.call('say ' + text, shell=True)
	# 	toSay = None
	# 	while not self.quit:
	# 		if self.end_time is not None:
	# 			# this is terrible, but keyboard interrupts are so terrible in this
	# 			while time.time() < self.end_time:
	# 				pass
	# 			# only 1 key pressed
	# 			if self.second_key is None:
	# 				# left press
	# 				if(self.first_key == 63234):
	# 					print("SINGLE LEFT PRESS")
	# 					self.selected_word = self.first_word["text"]
	# 					toSay = self.selected_word
	# 				# up press
	# 				elif(self.first_key == 63232):
	# 					print("SINGLE UP PRESS")
	# 					self.selected_word = self.second_word["text"]
	# 					toSay = self.selected_word
	# 				# down press
	# 				elif(self.first_key == 63235):
	# 					print("SINGLE RIGHT PRESS")
	# 					self.selected_word = self.third_word["text"]
	# 					toSay = self.selected_word
	# 				else:
	# 					self.selected_word = None
	# 					toSay = self.selected_word
	# 				self.first_key = None
	# 				self.end_time = None
	# 			# double click
	# 			elif self.first_key == self.second_key:
	# 				# left press
	# 				if(self.first_key == 63234):
	# 					print("DOUBLE LEFT PRESS")
	# 					# WE NEED TO RESOLVE GOING BACK!!! CIRCULAR DEPENDENCIES
	# 					UI_code.navigation.back_to_menu(self, True, 
	# 						self.num_words, self.sleeptime, self.clicktime)
	# 					self.quit = True
	# 				# up press
	# 				elif(self.fourth_word["text"] and self.first_key == 63232):
	# 					print("DOUBLE UP PRESS")
	# 					self.selected_word = self.fourth_word["text"]
	# 					toSay = self.selected_word
	# 				# down press
	# 				elif(self.fifth_word["text"] and self.first_key == 63235):
	# 					print("DOUBLE RIGHT PRESS")
	# 					self.selected_word = self.fifth_word["text"]
	# 					toSay = self.selected_word
	# 				else:
	# 					self.selected_word = None
	# 					toSay = self.selected_word
	# 				self.first_key = None
	# 				self.second_key = None
	# 				self.end_time = None
	# 			# assume first key press was a mistake, second key becomes first
	# 			# key and second key is reset to nothing
	# 			else:
	# 				self.end_time = time.time()
	# 				self.first_key = self.second_key
	# 				self.second_key = None

	# 			if toSay is not None:
	# 				# display the word
	# 				self.selected_word_label["text"] = toSay
	# 				self.selected_word_label["foreground"] = "black"
	# 				# say the word
	# 				subprocess.call('say ' + toSay, shell=True)
					




	def form_screen(self, controller):
		# set color to off-white
		self.configure(background="#FEFEFA")
		# set title of screen to none
		self.winfo_toplevel().title("")
		# cover full screen
		#self.cover_full_screen()
		# set titles
		self.load_titles(controller)
		# load arrows
		self.load_arrows()
		# load legend
		self.load_legend()


	def load_titles(self, controller):
		# get word predictions
		#word_predictions = tellnext.new_next_word(None, None)
		word_predictions = ["I", "How", "Hello",  "My", "Can"]
		self.first_word = word_predictions[0]
		self.second_word = word_predictions[1]
		self.third_word = word_predictions[2]
		if controller.num_words > 3:
			self.fourth_word = word_predictions[3]
		if controller.num_words > 4:
			self.fifth_word = word_predictions[4]
		# load titles
		title = Label(self, text="The Microphone is Listening", font=("Times New Roman", 40), fg="black", bg ="#FEFEFA")
		title.pack(fill=X)
		# back button - always there
		back_button = Label(self, text="Back", 
			font=("Times New Roman", 36), fg="black", bg="#ff8080", width=9)
		#back_button.place(relx=0.05, rely=0.54, height=55)
		back_button.place(x=140, y=260 , anchor="center")

		# first word
		self.first_word = Label(self, text=self.first_word, 
			font=("Times New Roman", 36), fg="black", width=9, bg="#80bfff")
		#self.first_word.place(relx=0.05, rely=0.44, height=55)
		self.first_word.place(x=140, y=200 , anchor="center")

		# second word
		self.second_word = Label(self, text=self.second_word, 
			font=("Times New Roman", 36), fg="black", width=9, bg="#80bfff")
		#self.second_word.place(rely=.17, relx=.365, height=55)
		self.second_word.place(x=400, y=100, anchor="center")

		# third word
		self.third_word = Label(self, text=self.third_word , 
			font=("Times New Roman", 36), fg="black", width=9, bg="#80bfff")
		#self.third_word.place(rely=0.44, relx=.675, height=55)
		self.third_word.place(x=660, y=200, anchor="center")

		# fourth word
		self.fourth_word = Label(self, text=self.fourth_word, 
			font=("Times New Roman", 36), fg="black", width=9, bg="#ff8080")
		#self.fourth_word.place(rely=.27, relx=.365, height=55)
		self.fourth_word.place(x=400, y=160, anchor="center")

		# fifth word
		self.fifth_word = Label(self, text=self.fifth_word, 
			font=("Times New Roman", 36), fg="black", width=9, bg="#ff8080")
		#self.fifth_word.place(rely=0.54, relx=.675, height=55)
		self.fifth_word.place(x=660, y=260, anchor="center")

		# last selected word
		self.selected_word_label = Label(self, text="", 
			font=("Times New Roman", 36), fg="black", width=9, borderwidth=1,
			relief="solid")
		#self.selected_word_label.place(rely=.7, relx=.6)
		self.selected_word_label.place(x= 660, y= 340, anchor="center")

		temp_label = Label(self, text="Selected Word", 
			font=("Times New Roman", 26), fg="black", bg="#FEFEFA", width=13, highlightthickness=0)
		#temp_label.place(rely=.83, relx=.58)
		temp_label.place(x=660, y=390, anchor="center")



	def load_legend(self): 
		legend_text = """
------------------------
|    Single Click = Blue  |
|  Double Click = Red   |
------------------------"""
		legend_frame = LabelFrame(self,text='Legend',padx=5, pady=5, 
			foreground="black", bg="#FEFEFA",font=("Times New Roman", 14))
		#legend_frame.place(relx=.1, rely=.67)
		legend_frame.place(x=400, y=335, anchor="center")
		legend_label = Label(legend_frame,text=legend_text, fg="black", bg="#FEFEFA",
			font=("Times New Roman", 14))
		legend_label.pack()

	def load_arrows(self):
		# arrow left
		canvas_left = Canvas(self, width=55, height=20,bg="#FEFEFA", highlightthickness=0)
		#canvas_left.place(relx=.38, rely=.525)
		canvas_left.place(x=320, y=230, anchor="center")

		left = canvas_left.create_line(5, 10, 55, 10, 
			arrow=tk.FIRST, fill="black", width=10)
		# arrow up
		canvas_up = Canvas(self, width=20, height=55, bg="#FEFEFA", highlightthickness=0)
		#canvas_up.place(relx=.5, rely=.4)
		canvas_up.place(x=400, y=218, anchor="center")
		up = canvas_up.create_line(10, 5, 10, 55, 
			arrow=tk.FIRST, fill="black", width=10)
		# arrow right
		canvas_right = Canvas(self, width=55, height=20, bg="#FEFEFA", highlightthickness=0)
		#canvas_right.place(relx=.59 , rely=.525)
		canvas_right.place(x=480, y=230, anchor="center")
		right = canvas_right.create_line(0, 10, 50, 10, 
			arrow=tk.LAST, fill="black", width=10)