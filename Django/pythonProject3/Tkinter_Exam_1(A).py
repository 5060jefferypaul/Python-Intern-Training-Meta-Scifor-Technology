# Using tkinter add filter ,lambda and other advance concept to display once click on the button

import tkinter as tk
from tkinter import messagebox
import random

Names = ["Jeffery", "Tibin", "Don", "Robert", "Jerin", "Rohan", "Joel", "Jerin", "Amal"]
Pick_Names = []

window = tk.Tk()
window.title("Random Name")
window.geometry("600x680")


def Filter_Names():
    Filter_Name = list(filter(lambda name: name.startswith("J"), Names))
    print(Filter_Name)
    messagebox.showinfo("Filtered Names", str(Filter_Name))


Label = tk.Label(window, text="Filter", bg="yellow")
Label.pack()

Filter_Button = tk.Button(window, text="Filter Names", bg="green", command=Filter_Names)
Filter_Button.pack()

Label = tk.Label(window, text="")
Label.pack()

window.mainloop()
