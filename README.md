# Brad1
Creating a custom word prediction software to help increase speaking tempo

# Instructions for Setup

	Our application is run off a a Raspberry Pi, which has been preloaded with the 
	software. You interact with our application through use of a custom-built
	footpedal, which has been attached to the Raspberry Pi. Both the Raspberry Pi and
	the footpedal should be in your posession prior to use. 

	The only setup required is to plug in and turn on the Raspberry Pi, and attach the loose
	HDMI cord from the Raspberry Pi to a computer monitor.

	The app should begin and you can interact with it using the footpedal

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

