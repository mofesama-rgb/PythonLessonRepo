# Instructions:
# 1. Write a program that asks the user to input a number. Use if, elif, and else to print whether the 
# number is positive, negative, or zero.
# 2. Write a program that asks the user for their name. Use a for loop to print each letter of their name 
# on a separate line, prefixed with "Letter: "
# 3. Set a secret password in your code (e.g., "python123"). Use a while loop to keep asking the user to 
# type the password until they get it correct. Once they get it right, print "Access Granted!".
# 4. Ask the user to enter a whole number. Use a for loop and range(1, 11) to display the multiplication
#  table for that number from 1 to 10.


print("===== EXERCISE 1: Positive, Negative, or Zero =====")
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


print("\n===== EXERCISE 2: Print each letter of name =====")
name = input("Enter your name: ")
for letter in name:
    print("Letter: " + letter)


print("\n===== EXERCISE 3: Secret Password =====")
secret_pass = "python123"
password = input("Enter the password: ")
while password != secret_pass:
    password = input("Incorrect password. Try again: ")
print("Access Granted!")


print("\n===== EXERCISE 4: Multiplication Table =====")
whole_number = int(input("Enter a whole number: "))
for number in range(1, 11):
    result = whole_number * number
    print(str(whole_number) + " x " + str(number) + " = " + str(result))