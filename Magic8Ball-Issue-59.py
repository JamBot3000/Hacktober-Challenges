import sys
import random

ans = False

while not ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers=[' As I see it, yes.', 'Ask again later.','Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.',' It is decidedly so.',
 'Most likely.', 'My reply is no', 'My sources say no.', 'Outlook not so good.','Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.','Very doubtful', 'Without a doubt.', 'Yes.', 'Yes – definitely.',
 'You may rely on it.']
    
    if question == "":
        sys.exit()
    
    else:
    	print(random.choice(answers));