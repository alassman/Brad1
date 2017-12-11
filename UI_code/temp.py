
	def load_titles(self, controller):
		# get word predictions
		#word_predictions = tellnext.new_next_word(None, None)
		word_predictions = ["I", "How", "Hello",  "My", "Can"]
		self.first_word = word_predictions[0]
		self.second_word = word_predictions[1]
		self.third_word = word_predictions[2]
		if controller.num_words > 3:
			self.fourth_word = word_predictions[3]
		if controller.num_words > 4:
			self.fifth_word = word_predictions[4]
		# load titles
		title = Label(self, text="The Microphone is Listening", font=("Times New Roman", 60), fg="black")
		title.pack(fill=X)
		# back button - always there
		back_button = Label(self, text="Back", 
			font=("Times New Roman", 48), fg="black", bg="#ff8080", width=10)
		#back_button.place(relx=0.05, rely=0.54, height=55)
		back_button.place(x=160, y=280 , anchor="center")

		# first word
		self.first_word = Label(self, text=self.first_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		#self.first_word.place(relx=0.05, rely=0.44, height=55)
		self.first_word.place(x=160, y=350 , anchor="center")

		# second word
		self.second_word = Label(self, text=self.second_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		#self.second_word.place(rely=.17, relx=.365, height=55)
		self.second_word.place(x=400, y=200, anchor="center")

		# third word
		self.third_word = Label(self, text=self.third_word , 
			font=("Times New Roman", 48), fg="black", width=10, bg="#80bfff")
		#self.third_word.place(rely=0.44, relx=.675, height=55)
		self.third.place(x=620, y=280, anchor="center")

		# fourth word
		self.fourth_word = Label(self, text=self.fourth_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		#self.fourth_word.place(rely=.27, relx=.365, height=55)
		self.fourth.place(x=400, y=300, anchor="center")

		# fifth word
		self.fifth_word = Label(self, text=self.fifth_word, 
			font=("Times New Roman", 48), fg="black", width=10, bg="#ff8080")
		#self.fifth_word.place(rely=0.54, relx=.675, height=55)
		self.fifth.place(x=620, y=350, anchor="center")

		# last selected word
		self.selected_word_label = Label(self, text="", 
			font=("Times New Roman", 48), fg="black", width=10, borderwidth=1,
			relief="solid")
		self.selected_word_label.place(rely=.7, relx=.6)
		temp_label = Label(self, text="Selected Word ^^^", 
			font=("Times New Roman", 36), fg="black", width=15)
		temp_label.place(rely=.83, relx=.58)




	def load_legend(self):
		legend_text = """
------------------------
|   Single Click = Blue   |
|  Double Click = Red   |
------------------------"""
		legend_frame = LabelFrame(self,text='Legend',padx=0, pady=5, 
			foreground="black", font=("Times New Roman", 24))
		#legend_frame.place(relx=.1, rely=.67)
		legend_frame.place(x=400, rely=350, anchor ="center")
		legend_label = Label(legend_frame,text=legend_text, fg="black",
			font=("Times New Roman", 24))
		legend_label.pack()


