from gtts import gTTS  # google text to speech conversion module
import time  # used to delay while loop to check for the file contents, on line 7.
from os.path import exists as file_exists  # checks if a txt file exists, used on line 5.

if file_exists('text_to_read.txt'):  # if the txt file exists
    while True:  # check the file has text and copy it into the variable mytext
        time.sleep(2)  # wait 2 to recheck the file for contents.
        f = open('text_to_read.txt', 'r')  # open the file
        mytext = f.read()  # copy the text into mytext variable
        f.close()  # close the file

        # passes the text variable and language to gTTS module
        convert_this = gTTS(text=mytext, lang='en')

        # saves the converted audio in a mp3 file named myaudio.mp3
        # saves in the same folder as this program on your computer
        convert_this.save("myaudio.mp3")



