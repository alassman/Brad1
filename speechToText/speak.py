#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import pyaudio as PyAudio
import speech_recognition as sr
import os
import _thread
from os import path

class Listener():
	"""docstring for Listener"""
	def __init__(self):
		super(Listener, self).__init__()
		self.speakAgain = False

		# self.pyaudio.PyAudio().open(format = pyaudio.paInt16,
		# 						channels =1,
		# 						input_device_index = 1,
		# 						input = True
		# )


	# def listen1(self):


	# 	#create global var of word so that main driver can access it
	# 	#global word
	# 	print("listening")
	# 	print("thread id in listen(): " + str(_thread.get_ident()))
	# 	while(1):
	# 		print("in while")
	# 		r = sr.Recognizer()
	# 		with 

	# 			#r.adjust_for_ambient_noise(source)

	# 			r.energy_threshold = 133.1662533217743				
	# 			#r.dynamic_energy_threshold = True  

	# 			print("listen")
	# 			audio = r.listen(source)
	# 			#audio = r.record(source, duration = 3)
	# 			print("done")
	# 		# with open("speechToText/microphone-results.wav", "wb") as f:
	# 		# 	f.write(audio.get_wav_data())



	# 		# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")
	# 		try:
	# 			word = r.recognize_google(audio)
	# 			print(word)

	# 			# if str is bytes:  # this version of Python uses bytes for strings (Python 2)
 #    #             	print(u"You said {}".format(word).encode("utf-8"))
	# 			# 	#print(word)
	# 			# else:  # this version of Python uses unicode for strings (Python 3+)
					
 #    #             	print("You said {}".format(value))

	# 			#return word

	# 		except sr.UnknownValueError:
	# 			self.speakAgain = True
	# 			print("Did not understand")

			#use the audio file as the audio source
			# with sr.AudioFile(AUDIO_FILE) as source:
			# 	audio = r.record(source)
			# 	try:
			# 		word = r.recognize_google(audio)
			# 		print(word)

			# 		return word

			# 	except sr.UnknownValueError:
			# 		self.speakAgain = True
			# 		print("Did not understand")


	def listen(self):
		r = sr.Recognizer()
		m = sr.Microphone()

		try:
			print("A moment of silence, please...")
			with m as source: r.adjust_for_ambient_noise(source)
			#print("Set minimum energy threshold to {}".format(r.energy_threshold))
			while True:
				value = ""
				print("Speak!")
				with m as source: audio = r.record(source, duration=3)
				print("Got it! Now to recognize it...")

				with open("speechToText/microphone-results.wav", "wb") as f:
					f.write(audio.get_wav_data())



				AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "microphone-results.wav")
				
				try:
					# recognize speech using Google Speech Recognition
					value = r.recognize_google(audio)

					print(value)

					# we need some special handling here to correctly print unicode characters to standard output
					if str is bytes:  # this version of Python uses bytes for strings (Python 2)
						print(u"You said {}".format(value).encode("utf-8"))
					else:  # this version of Python uses unicode for strings (Python 3+)
						print("You said {}".format(value))
				except sr.UnknownValueError:
					print("Oops! Didn't catch that")
				except sr.RequestError as e:
					print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
		
				return value
		except KeyboardInterrupt:
			pass

