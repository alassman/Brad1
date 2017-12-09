import tkinter as tk 
from UI_code.application_screen import applicationScreen
from UI_code.main_menu import MainMenu
from UI_code.settings import settingsScreen
from UI_code.tutorial import tutorialScreen
from button import Button
from tkinter import *
import time

doublePressTime = 0.5
current_frame = None
Left = 23
Up = 24
Right = 25

#Button()

#controller
class RunApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		Button()
		print("hello world")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight= 800)
		container.grid_rowconfigure(0, weight = 480)

		self.frames = {}

		self.init_frames("MainMenu", MainMenu, container)
		self.init_frames("applicationScreen", applicationScreen, container)
		self.init_frames("settingsScreen", settingsScreen, container)
		# self.init_frames("tutorialScreen", tutorialScreen, container)

		self.show_frame("MainMenu")


	def init_frames(self, name, F, container):
		frame = F(container, self)
		self.frames[name] = frame
		frame.grid(row = 0, column = 0, sticky ="nsew")


	def show_frame(self, cont):
		global current_frame
		frame = self.frames[cont]
		frame.tkraise()

		current_frame = frame

		# frame.buttonListener = ButtonListener(frame.clicktime)
		# frame.buttonListener.launch()
		#self.buttonListener = ButtonListener(self.clicktime)
		#self.buttonListener.launch()

		# try:
		# 	_thread.start_new_thread(frame.wait_on_button_signal, (self,))
		# except Exception as e:
		# 	print(e)

	def buttonPressed(self, channel, double):
		if channel == Left:
			left_button(double)
		elif channel == Right:
			right_button(double)
		else:
			up_button(double)


	def left_button(self, double):
		global current_frame
		
		if current_frame == MainMenu:
			self.show_frame("tutorialScreen")

		# elif current_frame == applicationScreen:

		# elif current_frame == settingsScreen:

		# elif current_frame == tutorialScreen:


	def right_button(self, double):
		global current_frame

		if current_frame == MainMenu:
			self.show_frame("settingsScreen")
		# elif current_frame == applicationScreen:

		# elif current_frame == settingsScreen:

		# elif current_frame == tutorialScreen:


	def up_button(self, double):
		global current_frame
		if current_frame == MainMenu:
			self.show_frame("applicationScreen")

		# elif current_frame == applicationScreen:

		# elif current_frame == settingsScreen:

		# elif current_frame == tutorialScreen:



def main():
	# menu = tk.Tk()
	# menu.geometry("800x480")
	# #menu.attributes('-fullscreen', True)
	# menu_frame = menuFrame()
	but = Button()
	app = RunApp()
	app.mainloop()
		
if __name__ == '__main__':
	main()














