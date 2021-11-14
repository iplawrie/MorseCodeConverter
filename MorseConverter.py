class MorseConverter:
    def __init__(self, dictionary):
        self.dict = dictionary

#add space after each letter and '/' after each word
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
            #each letter needs a space between
            #each word need " / " between
        return output

    # def unmorsify(self):
    #     return "todo, not implemented yet"
