class MorseConverter:
    def __init__(self, dictionary):
        self.dict = dictionary

    def morsify(self, text):
        output = ""
        length = len(text)
        for i in range(length):
            output += self.dict[text[i].upper()] + "_"
        return output
    # def unmorsify(self):
    #     return "todo, not implemented yet"
