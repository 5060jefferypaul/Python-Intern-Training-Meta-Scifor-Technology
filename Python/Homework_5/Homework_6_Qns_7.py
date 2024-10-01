# Nidhi has a bad habit of repeating the same word while typing.
# She wants a program that can remove duplicate phrases from paragraphs written by her.
# To help Nidhi write a python program that can connect with a text file and remove repeating words.


Sentence = input("Enter about You : ")

file = open("Nidhi.txt", "w")
file.write(Sentence)
file.close()

file = open("Nidhi.txt", "r")
Content = file.read()
file.close()

words= Content.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print(" ".join(unique_words))

# My Name is Jeffery Thomas Paul. My Email is jefferypaul196@gmail.com. I am 24 years old. I am a Intern Python
# Developer at Meta Scifor Technology.




