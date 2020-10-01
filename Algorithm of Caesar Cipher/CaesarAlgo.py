#A python program to illustrate Caesar Cipher Algorithm 
def caesarEncrypt(text,key): 
    result = "" 

    for i in range(len(text)): 
        character = text[i] 
  
        if (character.isupper()): 
            result += chr((ord(character) + key - 65) % 26 + 65) 
  
        else: 
            result += chr((ord(character) + key - 97) % 26 + 97) 
  
    return result 
  
text = "HappyHacktoberfest"
key = 4
print("Cipher: " + caesarEncrypt(text,key))
