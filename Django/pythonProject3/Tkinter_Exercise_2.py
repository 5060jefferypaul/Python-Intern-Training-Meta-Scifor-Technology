import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

Label = tk.Label(window, text="Simple Calculator", font=("Arial", 20))
Label.pack()

label1 = tk.Label(window, text="Enter the First Number: ")
label1.pack()
Entry1 = tk.Entry(window)
Entry1.pack()
label2 = tk.Label(window, text="Enter the Second Number: ")
label2.pack()
Entry2 = tk.Entry(window)
Entry2.pack()
label3 = tk.Label(window, text="Enter the Operator (+, -, *, /): ")
label3.pack()
Entry3 = tk.Entry(window)
Entry3.pack()


def Calculate():
    if Entry3.get() == "+":
        result = int(Entry1.get()) + int(Entry2.get())
    elif Entry3.get() == "-":
        result = int(Entry1.get()) - int(Entry2.get())
    elif Entry3.get() == "*":
        result = int(Entry1.get()) * int(Entry2.get())
    elif Entry3.get() == "/":
        result = int(Entry1.get()) / int(Entry2.get())
    else:
        result = "Invalid Operator"
    Result_label.config(text="Result = " + str(result))


Calculate_button = tk.Button(window, text="Calculate", command=Calculate)
Calculate_button.pack()

# Result display label
Result_label = tk.Label(window, text="Result = ")
Result_label.pack()

window.mainloop()
