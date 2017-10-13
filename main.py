import tkinter as tk 
from UI_code.application_screen import applicationScreen
from UI_code.main_menu import menuFrame
from UI_code.settings import settingsScreen
from UI_code.tutorial import tutorialScreen
from tkinter import *

def main():
	menu = tk.Tk()
	menu.attributes('-fullscreen', True)
	menu_frame = menuFrame(menu)
	menu.mainloop()
		
if __name__ == '__main__':
	main()
