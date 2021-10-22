import winsound
import time


class Sound:
    def __init__(self):
        self.prevChar = ""
        self.dot = None
        self.dash = None
        self.temporal = 0.1

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

    def playSound(self, text):
        self.prevChar = ""
        for character in text:
            time.sleep(self.temporal)
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


classSound = Sound()
classSound.playSound(".- .- .-  .- .- .-")
