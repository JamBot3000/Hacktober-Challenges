respond = ["You are absolutely not sure of this",
"This is relative",
"Great, try it out",
"Articles would help, check them out",
"This is no good start",
"There are beautiful things in life, smile", 
"That's funny","I have no specific idea on that",
"Yeah, you sure do",
"Thread carefully",
"You can ask friends too",
"Be hopeful",
"Ask google",
"Python is the best choice",
"With consistency, you'd scale through",
"Hold out help is near",
"Tech is awesome", 
"I can't understand you",
"Peers could be fail but it is no one's fault",
"Use your best",
"You could write them out and meditate"
"These are the rules, you can't change them",
"It helps the thought-process"]

import random
import time

  
def magic():
    print('Hi, enter your question:')
    quest=input()
    print('Thinking...')
    time.sleep(2)
    result=random.choice(respond)
    print (result,'\n')
    replay()

  

def replay():
    print('Would you like to ask another question? (Y/N)')
    user_input=input()
    
    if user_input.lower() == 'y':
        magic()
    elif user_input.lower() == 'q':
        print('Bye, see you soon')
    else:
        print('You have entered a wrong input')
            
magic()
        

    




