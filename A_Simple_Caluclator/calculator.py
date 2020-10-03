from tkinter import *
from tkinter import font
top=Tk()
top.geometry("210x305")
top.title("  CALCULATOR   ")
top.configure(background="grey")

var1=StringVar()
str1 = ""

def equal():
    try:
        global str1
        total=str(eval(str1))
        var1.set(total)
        str1=total
    except:
        var1.set("error")
        str1=""

def press(n):
    global str1 
    str1=str1+str(n)
    var1.set(str1)

def clear():
    global str1
    str1=""
    var1.set(str1)

e1=Entry(top,bd=6,textvariable=var1)
e1.grid(columnspan=10, ipadx=40)
var1.set("Enter your expression")

l1=Label(top,text="      ",height=2,bg="grey")
l1.grid(row=1,column=0)
b1=Button(top,text="C",width=5,height=2,bg="#f00000",bd=5,command=clear)
b1.grid(row=2,column=0)
b2=Button(top,text="%",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('%'))
b2.grid(row=2,column=1)
b3=Button(top,text="x^2",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('**2'))
b3.grid(row=2,column=2)
b4=Button(top,text="/",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('/'))
b4.grid(row=2,column=3)

b5=Button(top,text="7",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(7))
b5.grid(row=4,column=0)
b6=Button(top,text="8",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(8))
b6.grid(row=4,column=1)
b7=Button(top,text="9",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(9))
b7.grid(row=4,column=2)
b8=Button(top,text="*",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('*'))
b8.grid(row=4,column=3)

b9=Button(top,text="4",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(4))
b9.grid(row=5,column=0)
b10=Button(top,text="5",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(5))
b10.grid(row=5,column=1)
b11=Button(top,text="6",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(6))
b11.grid(row=5,column=2)
b12=Button(top,text="-",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('-'))
b12.grid(row=5,column=3)

b13=Button(top,text="1",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(1))
b13.grid(row=6,column=0)
b14=Button(top,text="2",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(2))
b14.grid(row=6,column=1)
b15=Button(top,text="3",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(3))
b15.grid(row=6,column=2)
b16=Button(top,text="+",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('+'))
b16.grid(row=6,column=3)

b17=Button(top,text="x^y",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('**'))
b17.grid(row=7,column=0)
b18=Button(top,text="0",width=5,height=2,bg="#ff00f0",bd=5,command=lambda:press(0))
b18.grid(row=7,column=1)
b19=Button(top,text="=",width=5,height=2,bg="#00f000",bd=5,command=equal)
b19.grid(row=7,column=3)
b20=Button(top,text=".",width=5,height=2,bg="#f0f0ff",bd=5,fg="red",command=lambda:press('.'))
b20.grid(row=7,column=2)
top.mainloop()
