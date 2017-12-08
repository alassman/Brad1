import tkinter as tk 
import UI_code.navigation # import startTutorial, startApplication, startSettings
import threadedDoublePress
from tkinter import *
from threadedDoublePress import ButtonListener
import _thread

'''
THEY SHOULD BE FRAMES NOT SEPARATE applications - maybe???
'''

class menuFrame(Frame):
	def __init__(self, parent=None, num_words=3, sleeptime=3, clicktime=1):
		Frame.__init__(self, parent)
		self.parent = parent
		self.sleeptime = sleeptime
		self.clicktime = clicktime
		self.num_words = num_words
		self.pack()
		self.form_screen()
		# launch button listener
		self.buttonListener = ButtonListener(self.clicktime)
		self.buttonListener.launch()
		print("trying to spawn a thread")
		try:
			_thread.start_new_thread(self.wait_on_button_signal, ())
		except Exception as e:
			print(e)

	def wait_on_button_signal(self):
		while True:
			# if there is a selection
			#print("selection:")
			if self.buttonListener.selection:
				print(self.buttonListener.selection)

				# left button was pressed
				if self.buttonListener.selection == 1:
					UI_code.navigation.startTutorial(self.parent, 
						self.num_words, self.sleeptime, self.clicktime)
				# up button was pressed
				elif self.buttonListener.selection == 2:
					UI_code.navigation.startApplication(self.parent,
						self.num_words, self.sleeptime, self.clicktime)
				# right button was pressed
				else:
					UI_code.navigation.startSettings(self.parent, 
						self.num_words, self.sleeptime, self.clicktime)
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
		self.load_arrows()


	def load_titles(self):
		title = Label(self.parent, text="Main Menu", font=("Times New Roman", 72), fg="black")
		#title.pack(fill=X)
		#title.place(rely=0, relx=.3)
		title.place(x = 400, y = 50, anchor="center")

		tutorial = Button(self.parent, text="Tutorial", 
			font=("Times New Roman", 48), fg="black", width=7, 
			command= lambda: UI_code.navigation.startTutorial(self.parent, 
				self.num_words, self.sleeptime, self.clicktime))
		#tutorial.place(relx=0.04, rely=0.5, height=55)
		tutorial.place(x = 160, y = 300, anchor="center")

		start = Button(self.parent, text="Start", 
			font=("Times New Roman", 48), fg="black", width=7, 
			command= lambda: UI_code.navigation.startApplication(self.parent,
				self.num_words, self.sleeptime, self.clicktime))
		#start.place(rely=.3, relx=.35, height=55)
		start.place(x = 400, y = 160, anchor="center")

		settings = Button(self.parent, text="Settings", 
			font=("Times New Roman", 48), fg="black", width=7, 
			command =lambda: UI_code.navigation.startSettings(self.parent, 
				self.num_words, self.sleeptime, self.clicktime))
		#settings.place(rely=0.5, relx=.66, height=55)

		settings.place(x = 620, y = 300, anchor="center")


	def load_arrows(self):
		# arrow left
		canvas_left = Canvas(self.parent, width=55, height=20)
		#canvas_left.place(relx=.38, rely=.525)

		canvas_left.place(x = 350, y = 310, anchor="center")

		left = canvas_left.create_line(5, 10, 55, 10, 
			arrow=tk.FIRST, fill="#FF0000", width=12)
		# arrow up
		canvas_up = Canvas(self.parent, width=20, height=55)
		#canvas_up.place(relx=.5, rely=.4)

		canvas_up.place(x = 400, y = 250, anchor="center")

		up = canvas_up.create_line(10, 5, 10, 55, 
			arrow=tk.FIRST, fill="#FF0000", width=12)
		# arrow right
		canvas_right = Canvas(self.parent, width=55, height=20)
		#canvas_right.place(relx=.59 , rely=.525)

		canvas_right.place(x = 450, y = 310, anchor="center")

		right = canvas_right.create_line(0, 10, 50, 10, 
			arrow=tk.LAST, fill="#FF0000", width=12)



