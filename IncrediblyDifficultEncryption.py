import codecs
print("Enter a string to undergo an incredibly difficult encoding process: ")

def xor(a, b):
    return bytes([_a ^ _b for _a, _b in zip(a, b)])

Word = input()
def encode(Word):
	Word = codecs.encode(Word, 'rot_13')
	Word = codecs.encode(Word, 'rot_13').encode()

	key = b'\x00' * len(Word)
	Word = xor(key,Word).decode() 
	return Word
print(Word)
