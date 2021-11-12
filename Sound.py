import winsound
import time
from gtts import gTTS
import os
import subprocess
# Real talk this has to be some of the jankiest code I've ever written. Don't blame me if your computer explodes. In
# order to play .mp3 files, which are generated by Google Text to Speech you will need FFmpeg located directly in
# your C drive. FFmpeg can be found here: ffmpeg.org/download.html
# If we end up doing this the probably illegal way, you can ignore this message.
# Since I imported os, you can probably edit the code in a pretty minor way to delete system32, so please don't.


class Sound:
    def __init__(self):
        self.prevChar = ""
        self.dot = None
        self.dash = None
        self.temporal = 0.2

    def getDot(self):
        return self.dot

    def setDot(self, dot):
        self.dot = dot

    def getDash(self):
        return self.dash

    def setDash(self, dash):
        self.dash = dash

    def setTime(self, temp):
        self.temporal = temp

    def getTime(self):
        return self.temporal

    def playText(self, toBePlayed):
        # This is some real jank. Essentially it checks if you have ffmpeg in the right place (if not it directs you
        # to the download). Next, it checks if it bugged out last time, and clears any possible leftover data to make
        # sure it doesn't bug out again. Then, it creates a mp3 file with the google text to speech audio. It then
        # converts that to a wav file. Next, it plays the wav file. Finally, it deletes both of the generated files.
        if os.path.exists('ffmpeg.exe'):
            if os.path.exists("tempFile.mp3"):
                os.remove("tempFile.mp3")
            if os.path.exists("tempFile.wav"):
                os.remove("tempFile.wav")
            soundObj = gTTS(text=toBePlayed, lang="en", slow=False)
            soundObj.save("tempFile.mp3")
            subprocess.run(['ffmpeg', '-i', 'tempFile.mp3', 'tempFile.wav'])
            winsound.PlaySound("tempFile.wav", winsound.SND_FILENAME)
            if os.path.exists("tempFile.mp3"):
                os.remove("tempFile.mp3")
            if os.path.exists("tempFile.wav"):
                os.remove("tempFile.wav")
        else:
            print("ffmpeg needs to be installed at C:/ffmpeg/bin/ffmpeg.exe")
            print("Get ffmpeg at ffmpeg.org/download.html")
            print("Be sure to unzip it directly into your C drive!")

    def playSound(self, text):
        self.prevChar = ""
        for character in text:
            if character == " ":
                if self.prevChar == " ":
                    time.sleep(self.temporal*4)
                else:
                    time.sleep(self.temporal*3)
            elif character == ".":
                if self.dot is None:
                    winsound.Beep(250, int(self.temporal*1000))
                    time.sleep(self.temporal)
                else:
                    winsound.PlaySound(self.dot, winsound.SND_FILENAME)
                    time.sleep(self.temporal)
            elif character == "-":
                if self.dash is None:
                    winsound.Beep(500, int(self.temporal*3000))
                    time.sleep(self.temporal)
                else:
                    winsound.PlaySound(self.dash, winsound.SND_FILENAME)
                    time.sleep(self.temporal)
            self.prevChar = character
        time.sleep(self.temporal)


classSound = Sound()
# classSound.playSound(".- .- .-  .- .- .-")
classSound.playText("Jeff Wall is the Zodiac Killer")