# text_to_speech_microservice

Reads the contents of a text file and converts it to audio. 

Be sure to open terminal and type: pip install gTTS to get the Google speech module for Python, as its not included with the Python installation. 

The file main.py checks to see if the txt files exists and if it does checks the file for contents. When there is something in the file to read it will convert it to speech. It will save the audio file in the same directory. It saves the audio as a .mp3 file. 

The file play_sound.py is an example of how you can play the saved .mp3 file in your program, if you want to. 
