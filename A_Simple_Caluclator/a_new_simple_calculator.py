#This simple calculator, calculates with the four basic operators, Addition "+",
# Subtraction "-", Multiplication "*" and Division "/"


response=['Welcome to smart calculator','My name is MONTY', 
		'Thanks for enjoy with me ','Sorry ,this is beyond my ability'] 

print('--------------'+response[0]+'------------') 

#A good title to start.
num1 = float(input ("enter your first number: "))
#float actually converted whatever the user inputed from a string to a number, either integer or decimal
op = input ("enter your operator ")
num2 = float(input ("enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("denominator can't be zero")
        quit()
    print(num1 / num2)
else:
    print("invalid operator")

# main python proghram                                       
#Execute it before asking values .

#response=['Welcome to smart calculator','My name is MONTY', 
	#	'Thanks for enjoy with me ','Sorry ,this is beyond my ability'] 

# fetching tokens from the text command 
def extract_from_text(text): 
	l=[] 
	for t in text.split(' '): 
		try: 
			l.append(float(t)) 
		except ValueError: 
			pass
	return l 

# calculating LCM 
def lcm(a,b): 
	L=a 
	if a>b else b 
	while L<=a*b: 
		if L%a==0 and L%b==0: 
			return L 
		L+=1

# calculating HCF 
def hcf(a,b): 
	H=a if a<b else b 
	while H>=1: 
		if a%H==0 and b%H==0: 
			return H 
		H-=1

# Addition 
def add(a,b): 
	return a+b 

# Subtraction 
def sub(a,b): 
	return a-b 

# Multiplication 
def mul(a,b): 
	return a*b 

# Division 
def div(a,b): 
	return a/b 

# Remainder 
def mod(a,b): 
	return a%b 

# Response to command 
# printing - "Thanks for enjoy with me" on exit 
def end(): 
	print(response[2]) 
	input('press enter key to exit') 
	exit() 

def myname(): 
	print(response[1]) 
def sorry(): 
	print(response[3]) 

# Operations - performed on the basis of text tokens 
operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add, 
			'SUB':sub,'SUBTRACT':sub, 'MINUS':sub, 
			'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf, 
			'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,       
			'DIVISION':div,'MOD':mod,'REMANDER'
			:mod,'MODULAS':mod} 

# commands 
commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end} 
		
#print('--------------'+response[0]+'------------') 

print('--------------'+response[1]+'--------------------') 


while True: 
	print() 
	text=input('enter your queries: ') 
	for word in text.split(' '): 
		if word.upper() in operations.keys(): 
			try: 
				l = extract_from_text(text) 
				r = operations[word.upper()] (l[0],l[1]) 
				print(r) 
			except: 
				print('something went wrong going plz enter again !!') 
			finally: 
					break
		elif word.upper() in commands.keys(): 
					commands[word.upper()]() 
					break
	else:		 
		sorry()
