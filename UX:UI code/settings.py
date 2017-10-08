import tkinter as tk 
from tkinter import *

class settingsScreen(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.parent = parent
		self.pack()
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
		title = Label(self.parent, text="Settings", font=("Times New Roman", 72), fg="black")
		title.pack(fill=X)