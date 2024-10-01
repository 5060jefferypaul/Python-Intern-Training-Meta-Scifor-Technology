# Priyanka wants to read a text file using python and
# she wants to print the content of that file in the terminal.
# But she is unable to specify the file name correctly.
# To help Priyanka write a program in python and show how to read the content of the text file
# and print it on the screen using python. ● Name of the text file: aboutPython.txt
# ● Content: ● Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
# It's high-level built in data structures, combined with dynamic typing and dynamic binding, ' \
#   'make it very attractive for Rapid Application Development, ' \
#   'as well as for use as a scripting or glue language to connect existing components together. ' \
#   'Python's simple, easy to learn syntax emphasizes readability and
# therefore reduces the cost of program maintenance. Python supports modules and packages,
# which encourages program modularity and code reuse. The Python interpreter and
# the extensive standard library are available in source or binary form without charge
# for all major platforms, and can be freely distributed. ● .
# ● Hint: ● Create a text file aboutPython.txt
# ● Copy the given content in that file
# ● Using python read the content of the file.
# ● Use the concept of file handling.

file = open("aboutPython.txt", "w")
file.write("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.\nIt's "
           "high-level built in data structures, combined with dynamic typing and dynamic binding,\nmake it very "
           "attractive for Rapid Application Development, as well as for use as a scripting or glue language to "
           "connect existing components together.\nPython's simple, easy to learn syntax emphasizes readability and "
           "therefore reduces the cost of program maintenance.\nPython supports modules and packages, which encourages "
           "program modularity and code-reuse.\nThe Python interpreter and the extensive standard library are available"
           "in source or binary form without charge for all major platforms,\nand can be freely distributed.")
file.close()
file = open("aboutPython.txt", "r")
content = file.read()
print(content)
