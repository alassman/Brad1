import tkinter as tk 
from UI_code.application_screen import applicationScreen
from UI_code.main_menu import MainMenu
from UI_code.settings import settingsScreen
from UI_code.tutorial import tutorialScreen
from ButtonListener import ButtonListener
from tkinter import *
import _thread


# def main():
# 	menu = tk.Tk()
# 	menu.geometry("800x480")
# 	#menu.attributes('-fullscreen', True)
# 	menu_frame = menuFrame(menu)
# 	menu.mainloop()
		
# if __name__ == '__main__':
# 	main()


#controller
class RunApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		#Button()
		#print("hello world")
		container = tk.Frame(self, bg="white")
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight= 800)
		container.grid_rowconfigure(0, weight = 480)

		self.sleeptime = 3
		self.clicktime = 3
		self.num_words = 1
		self.exploration = 0.5

		self.frames = {}

		self.init_frames("MainMenu", MainMenu, container)
		self.init_frames("applicationScreen", applicationScreen, container)
		self.init_frames("settingsScreen", settingsScreen, container)
		self.init_frames("tutorialScreen", tutorialScreen, container)

		self.cur_thread = None
		self.current_frame = None

		self.ButtonListener = ButtonListener()
		self.ButtonListener.launch()

		self.show_frame("MainMenu")


	def init_frames(self, name, F, container):
		frame = F(container, self)
		self.frames[name] = frame
		frame.grid(row = 0, column = 0, sticky ="nsew")


	def show_frame(self, cont):
		frame = self.frames[cont]
		
		if not self.current_frame == None:
			self.current_frame.screen = False

		frame.tkraise()
		frame.update()

		frame.screen = True

		self.current_frame = frame


		#frame.wait_on_button_signal(self)

		#start listener if main app
		if cont == "applicationScreen":
			_thread.start_new_thread(frame.listen_for_words, (self,))
			print("made listeing thread")


		# if not self.cur_thread == None:
		# 	self.cur_thread.exit()

		try:
			self.cur_thread = _thread.start_new_thread(frame.wait_on_button_signal, (self,))
		except Exception as e:
			print(e)

def main():
	app = RunApp()
	app.mainloop()
		
if __name__ == '__main__':
	main()














