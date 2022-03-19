from tkinter import *



master = Tk()
master.title("Calculator")
equation = ""
expression = ""
justCalculated = False
previousCalculation = 0
def pressed(num):
    global expression
    global previousCalculation
    global justCalculated

    if justCalculated == True and (str(num) == "^" or "-" or "+" or "*" or "/"):
        expression = str(previousCalculation) + str(num)
    else:
        expression = expression + str(num)
    equation.set(expression)
    justCalculated = False

def calculate():
    try:
        global expression
        global previousCalculation
        global justCalculated
        calculation = str(eval(expression))
        equation.set(calculation)
        expression = ""
        justCalculated = True
        previousCalculation = calculation
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set(expression)

#Defines and creates GUI
equation = StringVar()
text = Entry(master,width = 50, borderwidth= 5,textvariable=equation)
text.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

buttonClear = Button(master,text="AC",padx=35,pady=20,command=clear)
buttonClear.grid(row=1,column=0)

buttonSub = Button(master,text= "^",padx=40,pady=20,command=lambda: pressed("**"))
buttonSub.grid(row=1,column=1)

buttonSub = Button(master,text= "(",padx=40,pady=20,command=lambda: pressed("("))
buttonSub.grid(row=1,column=2)

buttonSub = Button(master,text= ")",padx=40,pady=20,command=lambda: pressed(")"))
buttonSub.grid(row=1,column=3)

button1 = Button(master,text= "1",padx=40,pady=20,command=lambda: pressed(1))
button1.grid(row=2,column=0)

button2 = Button(master,text= "2",padx=40,pady=20,command=lambda: pressed(2))
button2.grid(row=2,column=1)

button3 = Button(master,text= "3",padx=40,pady=20,command=lambda: pressed(3))
button3.grid(row=2,column=2)

button4 = Button(master,text= "4",padx=40,pady=20,command=lambda: pressed(4))
button4.grid(row=3,column=0)

button5 = Button(master,text= "5",padx=40,pady=20,command=lambda: pressed(5))
button5.grid(row=3,column=1)

button6 = Button(master,text= "6",padx=40,pady=20,command=lambda: pressed(6))
button6.grid(row=3,column=2)

button7 = Button(master,text= "7",padx=40,pady=20,command=lambda: pressed(7))
button7.grid(row=4,column=0)

button8 = Button(master,text= "8",padx=40,pady=20,command=lambda: pressed(8))
button8.grid(row=4,column=1)

button9 = Button(master,text= "9",padx=40,pady=20,command=lambda: pressed(9))
button9.grid(row=4,column=2)

button0 = Button(master,text= "0",padx=88,pady=20,command=lambda: pressed(0))
button0.grid(row=5,column=0,columnspan=2)

buttonDecimal = Button(master,text= ".",padx=40,pady=20,command=lambda: pressed("."))
buttonDecimal.grid(row=5,column=2,columnspan=1)

buttonAdd = Button(master,text= "+",padx=40,pady=20,command=lambda: pressed("+"))
buttonAdd.grid(row=2,column=3)

buttonSub = Button(master,text= "-",padx=40,pady=20,command=lambda: pressed("-"))
buttonSub.grid(row=3,column=3)

buttonDiv = Button(master,text= "/",padx=40,pady=20,command=lambda: pressed("/"))
buttonDiv.grid(row=4,column=3)

buttonMul = Button(master,text= "*",padx=40,pady=20,command=lambda: pressed("*"))
buttonMul.grid(row=5,column=3)

buttonEqual = Button(master,text= "=",padx=185,pady=20,command=calculate)
buttonEqual.grid(row=6,column=0, columnspan=4)
master.mainloop()
