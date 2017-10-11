import tkinter as tk 
import navigation
from navigation import *
from tkinter import *

'''
THEY SHOULD BE FRAMES NOT SEPARATE applications - maybe???
'''

class menuFrame(Frame):
	def __init__(self,parent=None):
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
		self.load_arrows()


		
	'''
	def cover_full_screen(self):
		# make it cover the entire screen
		w, h = menu.winfo_screenwidth(), menu.winfo_screenheight()
		menu.overrideredirect(1)
		menu.geometry("%dx%d+0-20" % (w, h))

		menu.focus_set() # <-- move focus to this widget
		menu.bind("<Escape>", lambda e: e.widget.quit())
	'''

	def load_titles(self):
		title = Label(self.parent, text="Main Menu", font=("Times New Roman", 72), fg="black")
		title.pack(fill=X)
		tutorial = Button(self.parent, text="Tutorial", 
			font=("Times New Roman", 48), fg="black", width=10, 
			command= lambda: startTutorial(self.parent))
		tutorial.place(relx=0.15, rely=0.5, height=55)
		start = Button(self.parent, text="Start", 
			font=("Times New Roman", 48), fg="black", width=10, 
			command= lambda: startApplication(self.parent))
		start.place(rely=.3, relx=.4, height=55)
		settings = Button(self.parent, text="Settings", 
			font=("Times New Roman", 48), fg="black", width=10, 
			command =lambda: startSettings(self.parent))
		settings.place(rely=0.5, relx=.65, height=55)

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



