import tkinter as tk
from tkinter import *


def Button_Pressed(num):
    global equation
    equation = equation + str(num)
    equation_label.set(equation)
def exponent_Button(e):
    global equation
    equation = equation + "**"
    equation_label.set(equation)



def clear_pressed(i):
    global equation
    equation=""
    equation_label.set(equation)

def equal_pressed(i):
    global equation

    try:
        total = str(eval(equation))
        if total != '0':
            equation_label.set(total)
            equation=total
        elif total == '0':
            equation=''
            equation_label.set('0')


    except ZeroDivisionError:
        equation_label.set("Cannot divide by 0")
        equation=""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation=""


def delete_pressed(i):
    global equation
    equation=equation.rstrip(equation[-1])
    equation_label.set(equation)

def num_KeyPressed(i):
    global equation
    equation= equation+i.char
    equation_label.set(equation)









main = Tk()
main.config(bg="black")
main.title("Calculator")
main.geometry("1000x1000")


equation= ""
equation_label= StringVar()

border=Frame(main, width=400, height=405, bg='black')
border.place(relx=.5,rely=.5,anchor=CENTER)


label=Label(main,textvariable=equation_label,width=29, height=3,font=20, bg="white")
label.place(relx=.5,rely=.35,anchor=CENTER)

frame = Frame(main)
frame.place(relx=.5,rely=.55,anchor=CENTER)

for i in range(10):
    main.bind(str(i),num_KeyPressed)

main.bind(str("+"),num_KeyPressed)
main.bind(str("-"),num_KeyPressed)
main.bind(str("*"),num_KeyPressed)
main.bind(str("/"),num_KeyPressed)
main.bind(str("%"),num_KeyPressed)
main.bind(str("^"),exponent_Button)
main.bind(str("."),num_KeyPressed)
main.bind(str("<Return>"),equal_pressed)
main.bind(str("<BackSpace>"),delete_pressed)
main.bind(str("c"),clear_pressed)







button1=Button(frame,text="1",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(1))
button1.grid(row=3, column=0)
frame.bind("1",button1)

button2=Button(frame,text="2",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(2))
button2.grid(row=3, column=1)

button3=Button(frame,text="3",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(3))
button3.grid(row=3, column=2)

button4=Button(frame,text="4",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(4))
button4.grid(row=2, column=0)

button5=Button(frame,text="5",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(5))
button5.grid(row=2, column=1)

button6=Button(frame,text="6",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(6))
button6.grid(row=2, column=2)

button7=Button(frame,text="7",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(7))
button7.grid(row=1, column=0)

button8=Button(frame,text="8",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(8))
button8.grid(row=1, column=1)

button9=Button(frame,text="9",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(9))
button9.grid(row=1, column=2)

button0=Button(frame,text="0",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed(0))
button0.grid(row=4, column=1)

c=Button(frame,text="C",fg="White",bg="Grey",width=8,height=3,command=lambda: clear_pressed("c"))
c.grid(row=0, column=0)

plus=Button(frame,text="+",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("+"))
plus.grid(row=0, column=3)

minus=Button(frame,text="-",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("-"))
minus.grid(row=1, column=3)

multiply=Button(frame,text="X",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("*"))
multiply.grid(row=2, column=3)

divide=Button(frame,text="/",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("/"))
divide.grid(row=3, column=3)

equal=Button(frame,text="=",fg="White",bg="Grey",width=8,height=3,command=lambda: equal_pressed("="))
equal.grid(row=4, column=3)

decimal=Button(frame,text=".",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("."))
decimal.grid(row=4, column=2)

delete=Button(frame,text="Delete",fg="White",bg="Grey",width=8,height=3,command=lambda: delete_pressed("<BackSpace>"))
delete.grid(row=0, column=1)

remainder=Button(frame,text="%",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("%"))
remainder.grid(row=0, column=2)

exponent=Button(frame,text="^",fg="White",bg="Grey",width=8,height=3,command=lambda: Button_Pressed("**"))
exponent.grid(row=4, column=0)


main.mainloop()