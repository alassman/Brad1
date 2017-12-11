import tkinter as tk 
import UI_code.navigation # import startTutorial, startApplication, startSettings
import threadedDoublePress
from tkinter import *
from threadedDoublePress import ButtonListener
import _thread

'''
THEY SHOULD BE FRAMES NOT SEPARATE applications - maybe???
'''

class MainMenu(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		#self = parent
		# self.sleeptime = sleeptime
		# self.clicktime = clicktime
		# self.num_words = num_words
		#self.pack()
		self.screen = False
		self.form_screen(controller)
		# launch button listener
		# controller.buttonListener = ButtonListener(self.clicktime)
		# controller.buttonListener.launch()
		# print("trying to spawn a thread")
		# try:
		# 	_thread.start_new_thread(self.wait_on_button_signal, ())
		# except Exception as e:
		# 	print(e)

	def wait_on_button_signal(self, controller):
		print("main menu wait")
		print(self.screen)

		controller.buttonListener.startListening(controller.clicktime)
		while self.screen:
			# print("selection:")
			if controller.buttonListener.selection:
				print(controller.buttonListener.selection)

				# left button was pressed
				if controller.buttonListener.selection == 1 or controller.buttonListener.selection == 4:
					controller.buttonListener.finishListening()
					print("tutorialScreen")
					controller.show_frame("tutorialScreen")
				# up button was pressed
				elif controller.buttonListener.selection == 2 or controller.buttonListener.selection == 5:
					controller.buttonListener.finishListening()
					print("applicationScreen")
					controller.show_frame("applicationScreen")
				# right button was pressed
				else:
					print("Settings")
					controller.buttonListener.finishListening()
					controller.show_frame("settingsScreen")

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


	def load_titles(self, controller):
		title = tk.Label(self, text="Main Menu", font=("Times New Roman", 72), fg="black", bg="#FEFEFA")
		#title.pack(fill=X)
		#title.place(rely=0, relx=.3)
		title.place(x = 400, y = 50, anchor="center")
		#title.pack()

		tutorial = tk.Button(self, text="Tutorial", 
			font=("Times New Roman", 48), fg="black", bg="#FEFEFA", width=7,
			command= lambda: controller.show_frame("tutorialScreen"))
		#tutorial.place(relx=0.04, rely=0.5, height=55)
		tutorial.place(x = 160, y = 300, anchor="center")
		#tutorial.pack()

		start = tk.Button(self, text="Start", 
			font=("Times New Roman", 48), fg="black", bg="#FEFEFA",width=7, 
			command= lambda: controller.show_frame("applicationScreen"))

		#start.place(rely=.3, relx=.35, height=55)
		start.place(x = 400, y = 160, anchor="center")
		#start.pack()

		settings = tk.Button(self, text="Settings", 
			font=("Times New Roman", 48), fg="black", bg="#FEFEFA",width=7, 
			command =lambda: controller.show_frame("settingsScreen"))
		#settings.place(rely=0.5, relx=.66, height=55)

		settings.place(x = 620, y = 300, anchor="center")
		#settings.pack()

	def load_arrows(self):
		# arrow left
		canvas_left = Canvas(self, width=55, height=20, bg="#FEFEFA", highlightthickness=0)
		#canvas_left.place(relx=.38, rely=.525)

		canvas_left.place(x = 350, y = 310, anchor="center")

		left = canvas_left.create_line(5, 10, 55, 10, 
			arrow=tk.FIRST, fill="black", width=12)
		# arrow up
		canvas_up = Canvas(self, width=20, height=55, bg="#FEFEFA", highlightthickness=0)
		#canvas_up.place(relx=.5, rely=.4)

		canvas_up.place(x = 400, y = 250, anchor="center")

		up = canvas_up.create_line(10, 5, 10, 55, 
			arrow=tk.FIRST, fill="black", width=12)
		# arrow right
		canvas_right = Canvas(self, width=55, height=20, bg="#FEFEFA", highlightthickness=0)
		#canvas_right.place(relx=.59 , rely=.525)

		canvas_right.place(x = 450, y = 310, anchor="center")

		right = canvas_right.create_line(0, 10, 50, 10, 
			arrow=tk.LAST, fill="black", width=12)




