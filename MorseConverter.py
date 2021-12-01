from MorseDict import MorseDict
from MorseDict import EngDict


class MorseConverter:
    def __init__(self):
        self.dict = MorseDict
        self.engDict = EngDict

    # add space after each letter and '/' after each word
    def morsify(self, text):
        output = ""
        length = len(text)
        for i in range(length):
            if i == len(text):
                output += self.dict[text[i].upper()]
            else:
                output += self.dict[text[i].upper()] + " "
        return output

    # def unmorsify(self):
    #     return "todo, not implemented yet"
    #         output += self.dict[text[i].upper()] + " "
    #     return output

    def unmorsify(self, text):
        output = ""
        length = len(text)
        word = ""
        for i in range(length):
            if text[i] == ' ':
                output += self.engDict[word]
                word = ''
            else:
                word += text[i]
                # output += list(self.dict.items())[text[i].upper()]
        return output

    #   todo, error handling on key errors
