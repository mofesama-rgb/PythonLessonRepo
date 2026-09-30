# # print(7 < 4)
# # var1 = "Effie"
# # var2 = " "
# # if var1 :
# #     print("True")
# # if var2 :
# #     print("True")
# # first_num = int(input("Enter first number: "))
# # second_num = int(input("Enter second number: "))
# # if first_num == second_num :
# #     print(first_num, "is equal to", second_num)
# # if first_num != second_num:
# #     print(f"{first_num} is not equal to {second_num}")
# # if first_num < second_num:
# #     print(f"{first_num} is less than {second_num}")
# # if first_num > second_num:
# #     print(f"{first_num} is greater than {second_num}")
# # if first_num >= second_num:
# #     print(f"{first_num} is greater than or equal to {second_num}")
# # if first_num <= second_num:
# #     print(f"{first_num} is less than or equal to {second_num}")
# # f = 3
# # print(1 <= f <= 5)
# # x = 10
# # print(1 <= x <= 5)
# # print(5 < 9, 5 <= 9, 5 > 9, 5 >= 9, 9 == 5, 5 != 9)
# numb1 = int(input("Enter first number: "))
# numb2 = int(input("Enter second number: "))
# numb3 = int(input("Enter third number: "))
# # min_numb = numb1
# # if numb2 < min_numb:
# #     min_numb = numb2
# # if numb3 < min_numb:
# #     min_numb = numb3
# # print(min_numb)
# print(max(numb1, numb2, numb3))

gender = "Female"
age = 70
if gender == "female" and age >= 65:
    print("Elderly Lady")

semester_average = 83
final_exam_variable = 95
if semester_average >= 90 or  final_exam_variable >= 90:
    print("Student A")

grade = 0
if not grade == -1:
    print(f"The next grade is {grade}")
if grade != -1:
    print(f"the next grade is {grade}")
print(bool(-1))
if not grade:
    print("False")
else:
    print("True")

# (Prime Factorization) A prime number is divisible only by itself and 1 (e.g., 2, 3, 5,
# 7, 11, 13, …). The prime factors of a number are a set of prime numbers that multiply to
# gether to result in the given number. Thus, if a number is a divider of the given number
# and also a prime number, it is a prime factor of the given number. Prime factorization is
# the search for all prime factors of a given number. Write a script that uses a trial and error
# approach to determine the prime factors of the number 1537.

#  (Rabbit Births) A farmer wants to keep track of the average number of rabbits born
# on his farm every month. He records the number of does (female rabbits) he has combined
# with the number rabbits born every month. Develop a sentinel-controlled-repetition
# script that prompts the user to input the number of does living in the farm and the number
# of rabbits born in a specific month. After processing all input information, the script
# should calculate and display the combined average number of rabbits born per doe.

# (Challenge: Fibonacci Sequence) In the Fibonacci sequence, each number is the
# sum of the two preceding ones. The first 10 Fibonacci numbers are as follows:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
# Write a script where a user inputs a position (a number) and the number in that position
# in the Fibonacci Sequence is displayed.