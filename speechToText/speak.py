#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os
from os import path


def listen():

	#create global var of word so that main driver can access it
	#global word
	print("listening")
	while(1):
		r = sr.Recognizer()
		with sr.Microphone(device_index = None, sample_rate = 48000) as source:
		    #r.energy_threshold = 4000

		    r.dynamic_energy_threshold = True  
		    print("listen")
		    audio = r.record(source, duration = 3)
		    print("done")
		with open("speechToText/microphone-results.wav", "wb") as f:
		    f.write(audio.get_wav_data())

		AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")

		# use the audio file as the audio source
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)
			try:
				word = r.recognize_google(audio)
				print(word)

				return word

			except sr.UnknownValueError:
				print("Did not understand")


