import tkinter as tk
from tkinter import *
from application_screen import applicationScreen
from settings import settingsScreen
from tutorial import tutorialScreen

def startSettings(root):
	root.destroy()
	settings = tk.Tk()
	settings.attributes('-fullscreen', True)
	settings_screen = settingsScreen(settings)
	settings.mainloop()

def startTutorial(root):
	root.destroy()
	tutorial = tk.Tk()
	tutorial.attributes('-fullscreen', True)
	tutorial_screen = tutorialScreen(tutorial)
	tutorial.mainloop()

def startApplication(root):
	root.destroy()
	app = tk.Tk()
	app.attributes('-fullscreen', True)
	application_screen = applicationScreen(app)
	app.mainloop()

def back_to_menu(root):
	root.destroy()
	main()