from MorseConverter import MorseConverter
from MorseDict import MorseDict

dictionary = MorseDict
conv = MorseConverter(dictionary)
print(conv.morsify("hello"))
