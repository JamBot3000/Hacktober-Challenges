print("A simple program to tell the love percentage betwwen two people on basis of their name." )
a=input("Enter your name ")
b=input("Enter your lover name")
c=0
if(len(a) == len(b)):
    c+=1
if(a[0]==b[0]):
    c+=1
if(a[len(a)-1]==b[len(b)-1]):
    c+=1
ans=(c/3)*100;
print("the love percentage between " + a + " " + b + "is ", end=" ")
print(ans, end=" ")
print("%")
