import os
 
while True:
    word = input('Enter a word to speak: ')
    os.system("flite -voice rms -t 'The word you entered is " + word + ". Good job!'")
 
