import tkinter as tk 
import application_screen, main_menu, settings, tutorial
from application_screen import applicationScreen
from main_menu import menuFrame
from settings import settingsScreen
from tutorial import tutorialScreen
from tkinter import *

def main():
	menu = tk.Tk()
	menu.attributes('-fullscreen', True)
	menu_frame = menuFrame(menu)
	menu.mainloop()
		
if __name__ == '__main__':
	main()
