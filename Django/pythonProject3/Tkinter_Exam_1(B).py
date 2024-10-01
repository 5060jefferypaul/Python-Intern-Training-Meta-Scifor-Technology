# Create a School Registration Form

import tkinter as tk

window = tk.Tk()
window.title("School Registration Form")
window.geometry("600x680")

Label_Title = tk.Label(window, text="School Registration Form", bg="yellow")
Label_Title.pack()


def register():
    name = Entry_Name.get()
    age = Entry_Age.get()
    gender = Entry_Gender.get()
    Class = Entry_Class.get()
    Address = Entry_Address.get()
    Phone = Entry_Phone.get()

    print("REGISTRATION SUCESSFULL")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Class:", Class)
    print("Address:", Address)
    print("Phone:", Phone)


Label_Name = tk.Label(window, text="Name")
Label_Name.pack()
Entry_Name = tk.Entry(window)
Entry_Name.pack()

Label_Age = tk.Label(window, text="Age")
Label_Age.pack()
Entry_Age = tk.Entry(window)
Entry_Age.pack()

Label_Gender = tk.Label(window, text="Gender")
Label_Gender.pack()
Entry_Gender = tk.Entry(window)
Entry_Gender.pack()

Label_Class = tk.Label(window, text="Class")
Label_Class.pack()
Entry_Class = tk.Entry(window)
Entry_Class.pack()

Label_Address = tk.Label(window, text="Email")
Label_Address.pack()
Entry_Address = tk.Entry(window)
Entry_Address.pack()

Label_Phone = tk.Label(window, text="Phone")
Label_Phone.pack()
Entry_Phone = tk.Entry(window)
Entry_Phone.pack()

Submit_Button = tk.Button(window, text="Submit", command=register)
Submit_Button.pack()

window.mainloop()
