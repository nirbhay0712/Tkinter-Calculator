from threading import get_ident
from tkinter import *
import math


root = Tk()
root.title('Simple Calculator')

text_area = Entry(root, width = 30)
text_area.grid(row=0,column=0, columnspan=4)
text_area.focus()
text_area.delete(0, END)
global NUMBER
global TEXT
def add():
    global NUMBER
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    global TEXT
    TEXT = '+'


def substract():
    global NUMBER
    global TEXT
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    TEXT = '-'

def multiply():
    global NUMBER
    global TEXT
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    TEXT = '*'

def divide():
    global NUMBER
    global TEXT
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    TEXT = '/'

def modulus():
    global NUMBER
    global TEXT
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    TEXT = '%'

def inverse():
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    NUMBER = 1/NUMBER
    text_area.insert(0, str(NUMBER))

def square():
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    NUMBER = math.pow(NUMBER, 2)
    text_area.insert(0, str(NUMBER))

def squareroot():
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    NUMBER = math.sqrt(NUMBER)
    text_area.insert(0, str(NUMBER))

def negate():
    NUMBER = float(text_area.get())
    text_area.delete(0, END)
    NUMBER = NUMBER * -1
    print(NUMBER)
    text_area.insert(0, str(NUMBER))



def equal():
    if TEXT == '+':
        number2 = float(text_area.get())
        text_area.delete(0, END)
        result = NUMBER + float(number2)
        print(result)
        text_area.insert(0,str(result))
    elif TEXT == '-':
        number2 = float(text_area.get())
        text_area.delete(0, END)
        result = NUMBER - float(number2)
        print(result)
        text_area.insert(0,str(result))
    elif TEXT == '*':
        number2 = float(text_area.get())
        text_area.delete(0, END)
        result = NUMBER * float(number2)
        print(result)
        text_area.insert(0,str(result))
    elif TEXT == '/':
        number2 = float(text_area.get())
        text_area.delete(0, END)
        result = NUMBER / float(number2)
        print(result)
        text_area.insert(0,str(result))
    elif TEXT == '%':
        number2 = float(text_area.get())
        text_area.delete(0, END)
        result = NUMBER % float(number2)
        print(result)
        text_area.insert(0,str(result))


def delete():
    NUMBER = (text_area.get())
    if NUMBER == 0:
        text_area.delete(0, END)
    if '.' not in NUMBER:
        NUMBER = int(int(NUMBER)/10)
        text_area.delete(0, END)
        text_area.insert(0, str(NUMBER))
    else:
        length = len(NUMBER)
        length -=1
        NUMBER = NUMBER[0:length]
        text_area.delete(0, END)
        text_area.insert(0,str(NUMBER) )


def button_click(number):
    temp = text_area.get()
    text_area.delete(0, END)
    next_number = str(temp) + str(number)
    text = text_area.insert(0,next_number)

def clear():
    text_area.delete(0, END)

def clear_all():
    text_area.delete(0, END)
    NUMBER =0
    TEXT = ''




#Lowest row of entry

button_invert = Button(root, text='+/-',pady=10,width=4, command=negate).grid(row=6,column=0)
button_0 = Button(root, text='0', pady=10,width=4,command=lambda:button_click(0)).grid(row=6,column=1)
button_decimal = Button(root, text='.', pady=10,width=4, command = lambda: button_click(".")).grid(row=6,column=2)
button_equal = Button(root, text='=', pady=10,width=4,fg='blue', command= equal).grid(row=6,column=3)

#Row 1
button_1 = Button(root, text='1', pady=10,width=4,command=lambda:button_click(1)).grid(row=5,column=0)
button_2 = Button(root, text='2', pady=10,width=4, command=lambda:button_click(2)).grid(row=5,column=1)
button_3 = Button(root, text='3', pady=10,width=4, command=lambda:button_click(3)).grid(row=5,column=2)
button_plus = Button(root, text='+', pady=10,width=4, command =add).grid(row=5,column=3)

#Row2

button_4 = Button(root, text='4', pady=10,width=4, command=lambda:button_click(4)).grid(row=4,column=0)
button_5 = Button(root, text='5', pady=10,width=4, command=lambda:button_click(5)).grid(row=4,column=1)
button_6 = Button(root, text='6', pady=10,width=4, command=lambda:button_click(6)).grid(row=4,column=2)
button_sub = Button(root, text='-', pady=10,width=4, command=substract).grid(row=4,column=3)

#row3

button_7 = Button(root, text='7', pady=10,width=4, command=lambda:button_click(7)).grid(row=3,column=0)
button_8 = Button(root, text='8', pady=10,width=4,command=lambda:button_click(8)).grid(row=3,column=1)
button_9 = Button(root, text='9', pady=10,width=4,command=lambda:button_click(9)).grid(row=3,column=2)
button_multipy = Button(root, text='X', pady=10,width=4, command = multiply).grid(row=3,column=3)

#row4

button_reciprocal = Button(root, text='1/x', pady=10,width=4, command=inverse).grid(row=2,column=0)
button_square = Button(root, text='x²', pady=10,width=4, command=square).grid(row=2,column=1)
button_square_root = Button(root, text='√x', pady=10,width=4, command = squareroot).grid(row=2,column=2)
button_devide = Button(root, text='/', pady=10,width=4, command = divide).grid(row=2,column=3)

#row5
button_mod = Button(root, text='%', pady=10,width=4, command=modulus).grid(row=1,column=0)
buttom_CE= Button(root, text='CE', pady=10,width=4, command = clear).grid(row=1,column=1)
button_C = Button(root, text='C', pady=10,width=4, command = clear_all).grid(row=1,column=2)
button_del= Button(root, text='DEL', pady=10,width=4, command = delete).grid(row=1,column=3)



root.mainloop()