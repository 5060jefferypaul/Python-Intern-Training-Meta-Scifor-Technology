import tkinter as tk
import random

window = tk.Tk()
window.title("RANDOM GENERATOR ")

label = tk.Label(window, text="", bg="yellow")
label.pack()


def random1():
    r = random.randint(1, 100)
    label.config(text=r)


button = tk.Button(window, text="click", bg="green", command=random1)
button.pack()

window.mainloop()
