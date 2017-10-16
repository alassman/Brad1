#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from os import path

word = ""

def main():
	#create global var of word so that main driver can access it
	global word

	r = sr.Recognizer()

	while(1):

		print(word)

		#r = sr.Recognizer()
		with sr.Microphone(device_index = None, sample_rate = 48000) as source:
		    #r.energy_threshold = 4000

		    r.adjust_for_ambient_noise(source, duration=2)
		    r.dynamic_energy_threshold = True  
		    #print("listen")
		    audio = r.record(source, duration = 1)
		    #print("done")

		with open("microphone-results.wav", "wb") as f:
		    f.write(audio.get_wav_data())


		AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

		# use the audio file as the audio source

		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)

			try:
				#print(r.recognize_sphinx(audio))
				
				#set global var
				word = r.recognize_sphinx(audio)

			except sr.UnknownValueError:
				print("Did not understand")

def listen():

	#create global var of word so that main driver can access it
	global word

	r = sr.Recognizer()

	while(1):

		print(word)

		#r = sr.Recognizer()
		with sr.Microphone(device_index = None, sample_rate = 48000) as source:
		    #r.energy_threshold = 4000

		    r.adjust_for_ambient_noise(source, duration=2)
		    r.dynamic_energy_threshold = True  
		    #print("listen")
		    audio = r.record(source, duration = 1)
		    #print("done")

		with open("microphone-results.wav", "wb") as f:
		    f.write(audio.get_wav_data())


		AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

		# use the audio file as the audio source

		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)

			try:
				#print(r.recognize_sphinx(audio))
				
				#set global var
				word = r.recognize_sphinx(audio)

			except sr.UnknownValueError:
				print("Did not understand")

if __name__ == "__main__":
	main()





