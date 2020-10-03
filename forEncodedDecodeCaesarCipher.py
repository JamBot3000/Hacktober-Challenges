ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_text):
	cipher_text = ''
	plain_text = plain_text.upper()
	for c in plain_text:
		if c == ' ' :
			cipher_text += ' '
		else :
			index = ALPHABET.find(c)
			index = (index+KEY)%len(ALPHABET)
			cipher_text += ALPHABET[index]	
		
	print(cipher_text)

def caesar_decrypt(cipher_text):

	plain_text = ''
	
	for c in cipher_text:
		if c == ' ' :
			plain_text += ' '

		else :
			index = ALPHABET.find(c)
			index = (index-KEY)%len(ALPHABET)
			plain_text += ALPHABET[index]
		
	print(plain_text)
	
if __name__ == "__main__":
	
	enc_msg = raw_input("enter message to encode in caesaer cipher: ")
	caesar_encrypt(enc_msg)
	
	dec_msg = raw_input("enter message to decode caesar cipher: ")
	caesar_decrypt(dec_msg.upper())	