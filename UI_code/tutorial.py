import tkinter as tk 
from tkinter import *

class tutorialScreen(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.parent = parent
		self.pack()
		self.form_screen()
		self.parent.bind("<KeyRelease>", self.on_button_press)

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
		title = Label(self.parent, text="Tutorial", font=("Times New Roman", 72), fg="black")
		title.pack(fill=X)
		text = "FOR THIS ALPHA VERSION,\nNAVIGATE THE MAIN\nAPPLICATION PAGE USING THE ARROW KEYS\nPRESS ANY KEY TO GO BACK TO THE MAIN MENU"
		instructions = Label(self.parent, text= text, font=("Times New Roman", 48), fg="black")
		instructions.place(relx=.05, rely=.4)

	# navigate back to the menu screen
	def on_button_press(self):
		pass