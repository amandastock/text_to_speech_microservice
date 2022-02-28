# CS361 Assignment: Text to Speech Microservice 

Reads the contents of a text file and converts it to audio. 

Be sure to open terminal and type: pip install gTTS to get the Google speech module for Python, as its not included with the Python installation. 

The file text_to_speech.py checks to see if the txt files exists and if it does checks the file for contents. When there is something in the file to read it will convert it to speech. It will save the audio file in the same directory. It saves the audio as a .mp3 file. It does not close, but keeps checking the txt file. 

The file play_sound.py is an example of how you can play the saved .mp3 file in your program, if you want to do it that way. Whenever you call play sound it will play whatever the current .mp3 is. There are other ways to play an audio file in python where you can pause and stop. 
