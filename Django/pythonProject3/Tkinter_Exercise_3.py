import tkinter as tk
from tkinter import IntVar
from tkinter import BooleanVar

# Create the main window
window = tk.Tk()
window.title("Registration Form for COVID Vaccine")
window.geometry("600x680")

# Title Label
title_label = tk.Label(window, text="Registration Form for COVID Vaccine", font=("Arial", 15))
title_label.pack()

label_name = tk.Label(window, text="Name of the Visitor: ")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_age = tk.Label(window, text="Age of the Visitor: ")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

label_gender = tk.Label(window, text="Gender: ")
label_gender.pack()
Gender_var = IntVar()
Gender_male = tk.Radiobutton(window, text="Male", variable=Gender_var, value=1)
Gender_male.pack()
Gender_female = tk.Radiobutton(window, text="Female", variable=Gender_var, value=2)
Gender_female.pack()
Gender_other = tk.Radiobutton(window, text="Other", variable=Gender_var, value=3)
Gender_other.pack(pady=5)

label_address = tk.Label(window, text="Address: ")
label_address.pack()
entry_address = tk.Text(window, height=4, width=40)
entry_address.pack()

label_email = tk.Label(window, text="Email Id: ")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

label_contact = tk.Label(window, text="Contact No: ")
label_contact.pack()
entry_contact = tk.Entry(window)
entry_contact.pack()

label_country = tk.Label(window, text="Country: ")
label_country.pack()
entry_country = tk.Entry(window)
entry_country.pack()

label_state = tk.Label(window, text="State: ")
label_state.pack()
entry_state = tk.Entry(window)
entry_state.pack()

label_disease = tk.Label(window, text="Select if you have any of the following diseases:")
label_disease.pack()
check_state1 = BooleanVar()
check_state2 = BooleanVar()
check_state3 = BooleanVar()
check_state4 = BooleanVar()
checkbox1 = tk.Checkbutton(window, text="Cold", variable=check_state1)
checkbox1.pack()
checkbox2 = tk.Checkbutton(window, text="Cough", variable=check_state2)
checkbox2.pack()
checkbox3 = tk.Checkbutton(window, text="Fever", variable=check_state3)
checkbox3.pack()
checkbox4 = tk.Checkbutton(window, text="Headache", variable=check_state4)
checkbox4.pack()

submit_button = tk.Button(window, text="Submit")
submit_button.pack(pady=10)

window.mainloop()
