class MorseConverter:
    def __init__(self, dictionary):
        self.dict = dictionary

#newline '\n' needs to be handled
    def morsify(self, text):
        output = ""
        length = len(text)
        for i in range(length):
            if text[i] == " ":
                output += "/ "
            elif i == len(text)-1:
                output += self.dict[text[i].upper()]
            else:
                output += self.dict[text[i].upper()] + " "
        return output

    # def unmorsify(self):
    #     return "todo, not implemented yet"
