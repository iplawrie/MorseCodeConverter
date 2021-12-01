from MorseConverter import MorseConverter
conv = MorseConverter()
print(conv.morsify("Hello World"))
print(conv.unmorsify(conv.morsify("Hello\n World")))
