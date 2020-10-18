def shopping_basket():
    from IPython.display import clear_output
    clear_output()
    pass
basket={}
tp=[]
print("  :: WELCOME TO SHOPPING_BASKET ::  ")
i=1

while(i!=0):
   
    print("enter your choice")
    print(" 1. To enter the item\n 2. To delete the item\n 3. To view the basket\n 4.Checkout\n 0. To exit")
    i=int(input())
    if(i==1):
        item=input("\nenter the name of the item you want to buy : ")
        quantity=int(input("enter the quantity of the respective item : "))
        price=int(input("enter the price\n"))
        basket.update({item:quantity})
        #basket = basket.append(item,quantity)
        total_price=price*quantity
        print("the total price of the {} is : {} ".format(item,total_price))
        tp.append(total_price)
    elif(i==2):
        item = input("enter the item to remove : ")
        x=0
        for x in basket:
            
            while x!=item:
                x=x+1
        tp.remove(tp.index(i))
        
        del basket[item]
        #tp.remove(total_price)
    elif(i==3):
        sum1=0
        print(basket)
        for i in basket.values():
        #print(i)
            sum1=sum1+i
        print(" total item in the basket is : {}".format(sum1))
        sum2=0
        for j in tp:
            sum2 = sum2 + j
        print(" total price of the basket is : {}".format(sum2))
        
        #for i in basket:
        #print(item,":",quantity)
        #print(basket.values().sum())
    elif(i==4):
        add = input("\nPlease enter your address you would like the goods to be delivered to : ")
        print("\ntotal of {} item worth Rs{} will be delivered to your address {} ".format(sum1,sum2,add))
        print("Thank you for shopping with us, hope you like the experience")
    else:    
        exit()
shopping_basket()
