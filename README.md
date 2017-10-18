# Brad1
Creating a custom word prediction software to help increase speaking tempo

# Instructions for Setup

You must run the following terminal commands on a Mac computer:

	1. /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		- The above install Homebrew for Mac

	2. sudo apt-get install python3-pip
		- The above installs pip3 for the Mac

	3. follow the instructions in the following link to configure sphinxbase and pocketsphinx
		- https://cmusphinx.github.io/wiki/tutorialpocketsphinx/

	4. brew install portaudio

	5. pip install pyaudio
		- The above install the requirement for using the microphone with the Mac

	6. pip install SpeechRecognition
		- The above installs the requirement for using the sphinx engine on the Mac

	7. pip install tkinter
		- This installs the tkinter package for building GUIs in Python
		
	8. navigate to the directory entitled "Brad1" and run: python main.py

# User Instructions:

	We ran into some of the issues with running the word prediction software on Mac. However, it works on Linux. 
	As of now, this program listens for words, and the words it hears populates the screen (instead of the
	predicted words). The arrows on the screen correspond to directional buttons on the keyboard, and selecting
	an arrow will cause the corresponding word to be said outloud. The program is constantly listening, so new 
	words will populate the screen every 5-10 seconds. 

	The word prediction is a standalone. Go to the mastadon folder and type ./bindict.py. If you get an error saying
	permission denied, please tpye $ chmod 777 *. This will give you read/write access to all files in the mastodon
	directory. Again, run ./bindict.py and you will be prompted to enter words for the prediction tree. Make sure
	the input is surrounded by quotation marks.



