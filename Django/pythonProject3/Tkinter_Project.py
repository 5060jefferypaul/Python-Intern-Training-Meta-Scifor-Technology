# In a coding class the teacher has taught the kids about the python GUI and
# has now assigned the following task to the students
#
# 1) Create a random name picker from a given list of students
#
# 2) should have a button clicking on which a random name should be picked
#
# 3) Once the random name is picked the name should be removed
# from the list so that the name is not repeated and also the removed name should show in completed section
# #create a GUI with two sections one to see the randomly generated name and the other one to see the names
# # that are generated randomly and which are not suppose to be considered for generating randomly again.


import tkinter as tk
import random

Student_Name = ["Jeffery", "Tibin", "Don", "Robert", "Jerin", "Rohan", "Joel", "Jerin", "Amal"]
Random_Name = []

window = tk.Tk()
window.title("Random Name Picker")
window.geometry("600x680")


def Random_Name_Picker():
    if Student_Name:
        random_name = random.choice(Student_Name)
        Random_Name.append(random_name)
        Student_Name.remove(random_name)
        Label.config(text=random_name)
    else:
        Label.config(text="No more names to pick")


Label = tk.Label(window, text="Random Name Generator", bg="yellow")
Label.pack()

Random_Button = tk.Button(window, text="Select a Random Name", bg="green", command=Random_Name_Picker)
Random_Button.pack()

Picked_Names = tk.Label(window, text="Picked Name : ")
Picked_Names.pack()

Label = tk.Label(window, text="")
Label.pack()

window.mainloop()
