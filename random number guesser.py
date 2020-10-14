def choose_rand():
    import random
    rand_num = random.randint(0,100)
    i = 0
    while i < 10:
        input_num = int(input("Guess a Number and Enter that Number here : "))
        if input_num < rand_num :
            print('the number you have guessed is smaller, please guess a larger number')
            i = i + 1
        
        elif input_num > rand_num : 
            print('the number you have guessed is bigger, please guess a smaller number')
            i = i + 1
            
            
        else:
            print('Congrats you have guessed the correct number :) in chances : ',i)
            i = 11
    if i == 10:
        
        print('sorry better luck next time, the number was :  ',rand_num)
        

choose_rand()
