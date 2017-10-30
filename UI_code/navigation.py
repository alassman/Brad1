import tkinter as tk
from tkinter import *
import UI_code.settings as settings_ui
import UI_code.application_screen
import UI_code.tutorial as tutorial_ui
import UI_code.main_menu
'''
from UI_code.application_screen import applicationScreen
from UI_code.settings import settingsScreen
from UI_code.tutorial import tutorialScreen
'''
# from UI_code.main_menu import menuFrame

def startSettings(root):
	root.destroy()
	settings = tk.Tk()
	settings.attributes('-fullscreen', True)
	settings_screen = settings_ui.settingsScreen(settings)
	settings.mainloop()

def startTutorial(root):
	root.destroy()
	tutorial = tk.Tk()
	tutorial.attributes('-fullscreen', True)
	tutorial_screen = tutorial_ui.tutorialScreen(tutorial)
	tutorial.mainloop()

def startApplication(root):
	root.destroy()
	app = tk.Tk()
	app.attributes('-fullscreen', True)
	application_screen = UI_code.application_screen.applicationScreen(app)
	app.mainloop()

def back_to_menu(root, from_app=False):
	if not from_app:
		root.destroy()
		menu = tk.Tk()
		menu.attributes('-fullscreen', True)
		menu_frame = UI_code.main_menu.menuFrame(menu)
		menu.mainloop()
	else:
		print("from main")
		root.destroy()
		menu = tk.Tk()
		menu.attributes('-fullscreen', True)
		menu_frame = UI_code.main_menu.menuFrame(menu)
		menu.mainloop()
	

	