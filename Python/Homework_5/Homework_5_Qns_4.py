# ● Arvind has a huge text file and he wants to put a serial number at the beginning of each line.
# Doing this task manually can take a lot of time. He is not aware of python file handling.
# Write a python program that can put a serial number in front of each line in any specified text file.

# ● Arvind has a huge text file and he wants to put a serial number at the beginning of each line.
# Doing this task manually can take a lot of time. He is not aware of python file handling.
# Write a python program that can put a serial number in front of each line in any specified text file.

file = open("Huge_Text_File.txt", "w")
file.write("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.\n It's "
           "high-level built in data structures, combined with dynamic typing and dynamic binding.\n Python's simple, "
           "easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.\n "
           "Python supports modules and packages, which encourages program modularity and code reuse. ")
file.close()


file = open("Huge_Text_File.txt", "r")
Content = file.readlines()
file.close()

Serial_Number = []
for i, Line in enumerate(Content, 1):
    Serial_Number.append(f"{i}. {Line}")

file = open("huge_file.txt", "w")
file.writelines(Serial_Number)
file.close()

for Line in Serial_Number:
    print(Line, end='')