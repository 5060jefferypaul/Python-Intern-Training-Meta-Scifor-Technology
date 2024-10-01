# ● Shubham had created a BMI calculator to check his health condition daily.
# But he is not able to record the values.
# He wants to see how his BMI is changing.
# So he decided to connect his BMI program with a text file using the concept of file handling.
# Now, when he uses his BMI program, his height, weight, BMI, and date get added to a text file "bmi.txt".
# Create a program that can do the same thing for you.


Height = float(input("Enter your Height in Centimeters: "))
Weight = float(input("Enter your Weight in Kilograms: "))
BMI = Weight/(Height/100)**2
print("Your BMI Calculated is:", BMI)

file = open("bmi.txt", "a")
file.write("Your Height is : {Height},Your Weight is : {Weight},Your BMI is : {BMI}\n")
file.close()
