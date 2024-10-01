# Arunima created a text file on programming where she wrote the word language incorrectly many times.
# Now she wants to replace the incorrect word with the correct word.
# Doing it manually can take a lot of time plus she can miss out few words at the end.
# To help Arunima to replace the words write a python program. Use the concept of file handling and make changes in the text file.

Sentence = input("Enter a sentence: ")
Wrong_Word = input("Enter the Wrong Word to Replace : ")
Correct_Word = input("Enter the Correct Word to Replace : ")

file = open("Programming.txt", "w")
file.write(Sentence)
file.close()

file = open("Programming.txt", "r")
Content = file.read()
file.close()

Content = Content.replace(Wrong_Word, Correct_Word)

file = open("Programming.txt", "w")
file.write(Content)
file.close()

file = open("Programming.txt", "r")
Content = file.read()
file.close()

print(Content)