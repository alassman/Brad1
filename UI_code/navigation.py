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

def startSettings(root, num_words, sleeptime, clicktime):
	root.destroy()
	settings = tk.Tk()
	settings.attributes('-fullscreen', True)
	settings_screen = settings_ui.settingsScreen(settings, num_words, sleeptime, clicktime)
	settings.mainloop()

def startTutorial(root, num_words, sleeptime, clicktime):
	root.destroy()
	tutorial = tk.Tk()
	tutorial.attributes('-fullscreen', True)
	tutorial_screen = tutorial_ui.tutorialScreen(tutorial, num_words, sleeptime, clicktime)
	tutorial.mainloop()

def startApplication(root, num_words, sleeptime, clicktime):
	root.destroy()
	app = tk.Tk()
	app.attributes('-fullscreen', True)
	application_screen = UI_code.application_screen.applicationScreen(app, 
		num_words, sleeptime, clicktime)
	app.mainloop()

def back_to_menu(root, from_app=False, num_words=None, sleeptime=None, clicktime=None):
	if not from_app:
		root.destroy()
		menu = tk.Tk()
		menu.attributes('-fullscreen', True)
		if (num_words is not None) and (sleeptime is not None) and (clicktime is not None):
			menu_frame = UI_code.main_menu.menuFrame(menu, num_words, sleeptime, clicktime)
			menu.mainloop()
		else:
			menu_frame = UI_code.main_menu.menuFrame(menu)
			menu.mainloop()
	else:
		print("from main")
		root.destroy()
		menu = tk.Tk()
		menu.attributes('-fullscreen', True)
		if (num_words is not None) and (sleeptime is not None) and (clicktime is not None):
			menu_frame = UI_code.main_menu.menuFrame(menu, num_words, sleeptime, clicktime)
		else:
			menu_frame = UI_code.main_menu.menuFrame(menu)
		menu.mainloop()
	

	