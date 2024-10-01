from tkinter import *
import math

window = Tk()
window.geometry("800x450")
window.title("CALCULATOR")
window.resizable(TRUE, FALSE)
window.configure(bg="peachpuff")

lb = Label(window, text="CALCULATOR", font="Tahoma 15 bold", fg="brown", bg="light blue")
lb.place(x=300, y=10, width=300, height=50)

button1 = Button(window, text="1", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("1"))
button1.place(x=140, y=150, width=60, height=40)
button2 = Button(window, text="2", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("2"))
button2.place(x=220, y=150, width=60, height=40)
button3 = Button(window, text="3", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("3"))
button3.place(x=300, y=150, width=60, height=40)
button4 = Button(window, text="/", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("/"))
button4.place(x=380, y=150, width=60, height=40)
button5 = Button(window, text="Sin", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("Sin("))
button5.place(x=460, y=150, width=60, height=40)
button6 = Button(window, text="%", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("%"))
button6.place(x=540, y=150, width=60, height=40)

button7 = Button(window, text="4", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("4"))
button7.place(x=140, y=200, width=60, height=40)
button8 = Button(window, text="5", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("5"))
button8.place(x=220, y=200, width=60, height=40)
button9 = Button(window, text="6", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("6"))
button9.place(x=300, y=200, width=60, height=40)
button10 = Button(window, text="-", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("-"))
button10.place(x=380, y=200, width=60, height=40)
button11 = Button(window, text="Cos", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("Cos("))
button11.place(x=460, y=200, width=60, height=40)
button12 = Button(window, text="*2", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("*2"))
button12.place(x=540, y=200, width=60, height=40)

button13 = Button(window, text="7", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("7"))
button13.place(x=140, y=250, width=60, height=40)
button14 = Button(window, text="8", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("8"))
button14.place(x=220, y=250, width=60, height=40)
button15 = Button(window, text="9", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("9"))
button15.place(x=300, y=250, width=60, height=40)
button16 = Button(window, text="+", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("+"))
button16.place(x=380, y=250, width=60, height=40)
button17 = Button(window, text="Tan", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("Tan("))
button17.place(x=460, y=250, width=60, height=40)
button18 = Button(window, text="*3", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("*3"))
button18.place(x=540, y=250, width=60, height=40)

button19 = Button(window, text=".", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("."))
button19.place(x=140, y=300, width=60, height=40)
button20 = Button(window, text="0", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("0"))
button20.place(x=220, y=300, width=60, height=40)
button21 = Button(window, text="*", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("*"))
button21.place(x=300, y=300, width=60, height=40)
button22 = Button(window, text="log", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("log("))
button22.place(x=380, y=300, width=60, height=40)

button23 = Button(window, text="=", font="Tahoma 14 bold", fg="white", bg="crimson", command=lambda: Solve())
button23.place(x=460, y=300, width=140, height=40)

button25 = Button(window, text="(", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show("("))
button25.place(x=620, y=150, width=60, height=40)
button26 = Button(window, text=")", font="Tahoma 13 bold", fg="white", bg="black", command=lambda: Show(")"))
button26.place(x=620, y=200, width=60, height=40)

calculator = ""


def Show(value):
    global calculator
    calculator += value
    t1.config(text=calculator)


def Clear():
    global calculator
    calculator = ""
    t1.config(text=calculator)


def Solve():
    global calculator

    if calculator != "":
        try:
            expression = calculator.replace("Sin", "math.sin")
            expression = expression.replace("Cos", "math.cos")
            expression = expression.replace("Tan", "math.tan")
            expression = expression.replace("log", "math.log")
            expression = expression.replace("sqrt", "math.sqrt")

            if expression.count('(') != expression.count(')'):
                raise ValueError("Unbalanced parentheses")

            Result = eval(expression)
            t1.config(text=Result)
        except SyntaxError:
            t1.config(text="SYNTAX ERROR")
        except ValueError as ve:
            t1.config(text=str(ve))
        except Exception as e:
            t1.config(text="ERROR")
    else:
        t1.config(text="")


button24 = Button(window, text="CLEAR", font="Tahoma 15 bold", fg="white", bg="lightcoral", command=lambda: Clear())
button24.place(x=140, y=350, width=540, height=40)

t1 = Label(window, font="Tahoma 15 bold", text="", anchor="e", bg="lightgray", fg="black")
t1.place(x=140, y=100, width=540, height=40)

window.mainloop()
