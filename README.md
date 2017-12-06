# Brad1
Creating a custom word prediction software to help increase speaking tempo

# Instructions for Setup

You must switch to desktop_version branch in order to run the version that runs on a computer.

You must run the following terminal commands on a Mac computer:

	1. /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		- The above install Homebrew for Mac

	2. sudo apt-get install python3-pip
		- The above installs pip3 for the Mac

	3. follow the instructions in the following link to configure sphinxbase and pocketsphinx
		- https://cmusphinx.github.io/wiki/tutorialpocketsphinx/

	4. brew install portaudio

	5. pip install pyaudio
		- The above installs the requirement for using the microphone with the Mac

	6. pip install SpeechRecognition
		- The above installs the requirement for using the sphinx engine on the Mac

	7. pip install tkinter
		- This installs the tkinter package for building GUIs in Python
		
	8. follow the instructions in the following link to install NLTK (version >= 3.0)
		- http://www.nltk.org/install.html
	
	9. pip install langdetect
		- The above installs the requirement for using tellnext word prediction
			
	8. navigate to the directory entitled "Brad1" and run: python main.py

# User Instructions:

	This is a word prediction program, navigated via a custom foot pedal. For this release, the foot pedal
	is not integrated into the system, but it is complete. As of now, the program starts with populated
	predicted words. Simultaneously, the program listens for words, and the words it hears are sent to the
	word prediction software. The arrows on the screen correspond to directional buttons on the keyboard, and selecting
	an arrow will cause the corresponding word to be said outloud. 
	
	In addition, there is a tutorial which walks the user through the flow of the system. There are also customizable 
	settings which can be changed at any time. 

# Note

	Originally we were thinking about training Brad's voice with Sphinx. However, we found that the Google recogintion is
	significantly better, with a 76% accuracy.

