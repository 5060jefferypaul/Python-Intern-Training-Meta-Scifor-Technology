# Himanshi has a text file and she wants to check whether that file contains any numerical value.
# So to help Himanshi
# write a python program that can check whether the text file includes any numerical value or not.
# As text files contain so many lines, so print the line number that has numerical values


file = open("File_Name.txt", "w")
file.write("My Name is Jeffery Thomas Paul.\nAnd my email is jefferypaul196@gmail.com.\nMy Phone number is 9496889")
file.close()
file = open("File_Name.txt", "r")
content = file.readlines()
Number_of_lines = 0

for line in content:
    Number_of_lines += 1
    if any(char.isdigit() for char in line):
        print(f"Line Number Which has Numerical Value is  {Number_of_lines}: {line}")
file.close()

