from tkinter import *

root=Tk()
root.title("Simple Calculator")

def Click(number):
    current=Enty.get()
    Enty.delete(0,END)
    Enty.insert(0,str(current)+str(number))

def Clear():
    Enty.delete(0,END)

def Add():
    FistNumber=Enty.get()
    global f_num
    global Sign
    Sign="Addition"
    f_num= int(FistNumber)
    Enty.delete(0,END)

def Equal():
    s_num=Enty.get()
    Enty.delete(0,END)
    if Sign=="Addition":
        Enty.insert(0, f_num + int(s_num))
    if Sign=="Subtraction":
        Enty.insert(0, f_num - int(s_num))
    if Sign=="Multiplication":
        Enty.insert(0, f_num * int(s_num))
    if Sign=="Division":
        Enty.insert(0, f_num / int(s_num))

def Subtract():
    FistNumber=Enty.get()
    global f_num
    global Sign
    Sign="Subtraction" 
    f_num= int(FistNumber)
    Enty.delete(0,END)

def Divide():
    FistNumber=Enty.get()
    global f_num
    global Sign
    Sign="Division" 
    f_num= int(FistNumber)
    Enty.delete(0,END)

def Multiply():
    FistNumber=Enty.get()
    global f_num
    global Sign
    Sign="Multiplication" 
    f_num= int(FistNumber)
    Enty.delete(0,END)

Enty=Entry(root,width=40,borderwidth=5)
Enty.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#initialization of buttons
button_1=Button(root,text="1",padx=40,pady=30,command=(lambda: Click(1)))
button_2=Button(root,text="2",padx=40,pady=30,command=(lambda: Click(2)))
button_3=Button(root,text="3",padx=40,pady=30,command=(lambda: Click(3)))
button_4=Button(root,text="4",padx=40,pady=30,command=(lambda: Click(4)))
button_5=Button(root,text="5",padx=40,pady=30,command=(lambda: Click(5)))
button_6=Button(root,text="6",padx=40,pady=30,command=(lambda: Click(6)))
button_7=Button(root,text="7",padx=40,pady=30,command=(lambda: Click(7)))
button_8=Button(root,text="8",padx=40,pady=30,command=(lambda: Click(8)))
button_9=Button(root,text="9",padx=40,pady=30,command=(lambda: Click(9)))
button_0=Button(root,text="0",padx=40,pady=30,command=(lambda: Click(0)))

button_equal=Button(root,text="=",padx=91,pady=30,command=Equal)
button_Add=Button(root,text="+",padx=39,pady=30,command=Add)
button_clear=Button(root,text="Clear",padx=79,pady=30,command=Clear)       #padding is changed due to the text inside the buttons 

button_subtract=Button(root,text="-",padx=40,pady=30,command=Subtract)
button_divide=Button(root,text="/",padx=40,pady=30,command=Divide)
button_multiply=Button(root,text="*",padx=40,pady=30,command=Multiply)

#Arranging the buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_Add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)

root.mainloop()
