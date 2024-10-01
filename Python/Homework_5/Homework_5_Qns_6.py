# ● Ayman wants to modify one of his text files. In his text file,
# he wants to start a new line whenever he encounters a number followed by a period(.).
#  So he decides to do the same with the help of the python program. Write a program for Ayman.


Sentence = input("Enter a Paragraph : ")
file = open("Ayman.txt", "w")
file.write(Sentence)
file.close()

file = open("Ayman.txt", "r")
Content = file.read()
file.close()

Content = Content.replace(".", "\n")

file = open("Ayman.txt", "w")
file.write(Content)
file.close()

file = open("Ayman.txt", "r")
Content = file.read()
file.close()

print(Content)

# About Myself .1) My Name is Jeffery Thomas Paul.2) My email is jefferypaul196@gmail.com.3) My Phone number is
# 9496889.4) I am 24 years old.5) I am a Intern Python Developer at Meta Scifor Technology.