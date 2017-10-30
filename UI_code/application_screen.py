import tkinter as tk 
import _thread, time, os
import subprocess
import tty, termios, sys
import UI_code.navigation
from tkinter import *
from speechToText.speak import listen
# from mastodon.bindict import BinaryDictionary

class applicationScreen(Frame):
	def __init__(self, parent=None, num_words=3, mic_sleep=3, clicktime=1):
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
		self.t1 = _thread.start_new_thread(self.listen_for_words, ())
		#_thread.start_new_thread(self.listen_for_button_press, ())
		self.pack()
		self.form_screen()
		# alpha code only
		self.first_key = None
		self.second_key = None
		self.end_time = None
		self.quit = False
		self.parent.bind("<KeyRelease>", self.on_button_press)
		self.t2 = _thread.start_new_thread(self.wait_on_button_press, ())


	def listen_for_words(self):
		# establish binary dictionary for later prediction
		path = os.getcwd() + "/mastodon/fiction.dict"
		#binary_dict = BinaryDictionary.from_file(path)
		while not self.quit:
			# no word on screen was selected
			if self.selected_word is None:
				# call Jenny's function to hear from microphone
				words_from_mic = listen()
				# parse words from Jenny's function
				words_list = words_from_mic.split()
				# call Lihu's function
				#word_predictions = binary_dict.get_predictions_five_words(words_list,
					#self.num_words)
			# predict word from selected word on screen
			else:
				# append to words_list
				words_list.append[self.selected_word]
				# call Lihu's function
				#word_predictions = binary_dict.get_predictions_five_words(words_list, 
					#self.num_words)
				# set the selected word to None
				self.selected_word = None
			# update the labels --> THIS NEEDS TO USE LIHU's PREDICTION
			if len(words_list) > 0:
				self.first_word["text"] = words_list[0]
			if len(words_list) > 1:
				self.second_word["text"] = words_list[1]
			if len(words_list) > 2:
				self.third_word["text"] = words_list[2]
			if len(words_list) > 3:
				self.fourth_word["text"] = words_list[3]
			if len(words_list) > 4:
				self.fifth_word["text"] = words_list[4]
			# sleep for 5 seconds before listening again
			time.sleep(self.sleeptime)
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
		#'''engine = pyttsx.init()
		#engine.say("HELLO WORLD I AM INITIALIZED, MY NAME IS ALFRED")
		#engine.runAndWait()'''
		#text = "HELLO WORLD I AM INITIALIZED, MY NAME IS ALFRED"
		#subprocess.call('say ' + text, shell=True)
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
					# up press
					elif(self.first_key == 63232):
						print("SINGLE UP PRESS")
						self.selected_word = self.second_word["text"]
					# down press
					elif(self.first_key == 63235):
						print("SINGLE RIGHT PRESS")
						self.selected_word = self.third_word["text"]
					else:
						self.selected_word = None
					self.first_key = None
					self.end_time = None
				# double click
				elif self.first_key == self.second_key:
					# left press
					if(self.first_key == 63234):
						print("DOUBLE LEFT PRESS")
						# WE NEED TO RESOLVE GOING BACK!!! CIRCULAR DEPENDENCIES
						UI_code.navigation.back_to_menu(self.parent, True)
						self.quit = True
					# up press
					elif(self.fourth_word["text"] and self.first_key == 63232):
						print("DOUBLE UP PRESS")
						self.selected_word = self.fourth_word["text"]
					# down press
					elif(self.fifth_word["text"] and self.first_key == 63235):
						print("DOUBLE RIGHT PRESS")
						self.selected_word = self.fifth_word["text"]
					else:
						self.selected_word = None
					self.first_key = None
					self.second_key = None
					self.end_time = None
				# assume first key press was a mistake, second key becomes first
				# key and second key is reset to nothing
				else:
					self.end_time = time.time()
					self.first_key = self.second_key
					self.second_key = None

				if self.selected_word is not None:
					subprocess.call('say ' + self.selected_word, shell=True)
				

	'''
	def listen_for_button_press(self):
		print("I AM IN THIS FUNCTION")
		# fill in with code to interact with Adam's raspberry pi
		# map directions to the words
		
		while True:
			if first_key is None:
				#first_key = sys.stdin.read(1)
				#first_key = ord( first_key )
				first_key = key_in()
				print("YOU Pressed" + str(first_key))
			else:
				end = time.time() + 1
				while time.time() < end:
					second_key = sys.stdin.read(1)
					second_key = ord( second_key[0] )
				# only 1 key pressed
				if second_key is None:
					# left press
					if(first_key == 37):
						print("SINGLE LEFT PRESS")
					# up press
					elif(first_key == 38):
						print("SINGLE UP PRESS")
					# down press
					elif(first_key == 39):
						print("SINGLE RIGHT PRESS")
					first_key = None
				# double click
				elif first_key == second_key:
					# left press
					if(first_key == 37):
						print("DOUBLE LEFT PRESS")
					# up press
					elif(first_key == 38):
						print("DOUBLE UP PRESS")
					# down press
					elif(first_key == 39):
						print("DOUBLE RIGHT PRESS")
					first_key = None
					second_key = None
				# assume first key press was a mistake, second key becomes first
				# key and second key is reset to nothing
				else:
					first_key = second_key
					second_key = None
		'''



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
		title = Label(self.parent, text="The Microphone is Listening", font=("Times New Roman", 72), fg="black")
		title.pack(fill=X)
		# back button - always there
		back_button = Label(self.parent, text="Back", 
			font=("Times New Roman", 48), fg="black", bg="#ff8080", width=10)
		back_button.place(relx=0.15, rely=0.6, height=55)
		# first word
		self.first_word = Label(self.parent, text=self.first_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		self.first_word.place(relx=0.15, rely=0.5, height=55)
		# second word
		self.second_word = Label(self.parent, text=self.second_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		self.second_word.place(rely=.2, relx=.4, height=55)
		# third word
		self.third_word = Label(self.parent, text=self.third_word , 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		self.third_word.place(rely=0.5, relx=.65, height=55)
		# fourth word
		self.fourth_word = Label(self.parent, text=self.fourth_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		self.fourth_word.place(rely=.3, relx=.4, height=55)
		# fifth word
		self.fifth_word = Label(self.parent, text=self.fifth_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		self.fifth_word.place(rely=0.6, relx=.65, height=55)

	def load_legend(self):
		legend_text = """
------------------------
|   Single Click = Blue   |
|  Double Click = Red   |
------------------------"""
		legend_frame = LabelFrame(self.parent,text='Legend',padx=5, pady=5, 
			foreground="black", font=("Times New Roman", 24))
		legend_frame.place(relx=.4, rely=.7)
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