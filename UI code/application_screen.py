import tkinter as tk 
import _thread
from tkinter import *

class applicationScreen(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.parent = parent
		self.first_word = None
		self.second_word = None
		self.third_word = None
		self.fourth_word = None
		self.fifth_word = None
		_thread.start_new_thread(self.listen_for_words, ())
		_thread.start_new_thread(self.listen_for_button_press, ())
		self.pack()
		self.form_screen()

	def listen_for_words(self):
		# fill in with code from Jenny
		# set all four word variables
		pass

	def send_word(self):
		# send the chosen word to Lihu's code
		pass

	def listen_for_button_press(self):
		# fill in with code to interact with Adam's raspberry pi
		# map directions to the words
		pass

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
		first_word = Label(self.parent, text="Where", 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		first_word.place(relx=0.15, rely=0.5, height=55)
		# second word
		second_word = Label(self.parent, text="Are", 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		second_word.place(rely=.2, relx=.4, height=55)
		# third word
		third_word = Label(self.parent, text= "Michigan" , 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		third_word.place(rely=0.5, relx=.65, height=55)
		# fourth word
		fourth_word = Label(self.parent, text="Helloy", 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		fourth_word.place(rely=.3, relx=.4, height=55)
		# fifth word
		fifth_word = Label(self.parent, text="You", 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		fifth_word.place(rely=0.6, relx=.65, height=55)

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