'''
Caesar Cipher encoder, input string and shift and it will output the encoded version of the string
'''

from sys import argv

alphabet = "abcdefghijklmnopqrstuvwxyz"

def CaesarCipherShift(stringParam, shiftParam):
    newString = ""
    stringParam.lower() # too tired to make it upper and lower case but could easily be done rip sorry
    for char in stringParam:
        try:
            newChar = alphabet[alphabet.index(char) + shiftParam]
            newString = newString + newChar
        except IndexError:
            indexValue = shiftParam - (25 - alphabet.index(char))
            newChar = alphabet[indexValue]
            newString = newString + newChar
        except ValueError:
            newString = newString + char
    print(newString)

# sorry jamie i used your code xxx
if len(argv) < 2 or int(argv[-1]) == 0:
    print("Usage: ./caesar-cipher.py <string> <shift>") # no quotation marks pls
    exit()
else:
    CaesarCipherShift(str(argv[1]), int(argv[2]))

# lmao i just realised that if i used ascii equivalents it would be way easier oops
# but it's 1:36am and i cannot keep my eyes open lolol      