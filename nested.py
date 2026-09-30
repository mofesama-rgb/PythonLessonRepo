# passes = 0
# failures = 0

# for student in range(10):
#     result = int(input("Enter student result. 1 = pass, 2 = fail: "))

#     if result == 1:
#         passes += 1
#     else:
#         failures += 1

# print(f"Number of students who passed: {passes}")
# print(f"Nuber of students who failed: {failures}")

# if passes > 8:
#     print("Bonus to instructor")

# write a for loop to collect two integers thenuse a nested if else statement to display wheter a value is 
# even or odd

# for i in range(2):
#     number = int(input("Enter an integer: "))

#     if number >= 0:
#         if number % 2 ==0:
#             print(f"{number} is even")
#         else:
#             print(f"{number} is odd")
#     else:
#         print(f"{number} is invalid")

# for number in range(10, 0, 2):
#     print(number, end=" ")
# amount = 121.34
# print(amount)
# print(f"{amount:.20f}")
# # import decimal
# from decimal import Decimal
# principal = Decimal("1000.00")
# print(principal)
# from decimal import Decimal as dc
# rate = dc("0.05")
# print(rate)
# A person invests $1000 in a savings account yielding 5% interest. Assuming that
# the person leaves all interest on deposit in the account, calculate and display the
# amount of money in the account at the end of each year for 10 years. Use the fol
# lowing formula for determining these amounts:
# a = p(1 + r)n
# where
# p is the original amount invested (i.e., the principal),
# r is the annual interest rate,
# n is the number of years and
# a is the amount on deposit at the end of the nth year.

# principal = Decimal("1000.00")
# rate = dc("0.05")
# for year in range(1, 11):
#     amount = principal *(1 + rate) **year
#     # print(f"{year:>2}{amount:>10.2f}")

# for number in range(100):
#     if number == 10:
#         break
#     print(number, end=" ")

for data in range(30):
    if data ==7:
        continue
    print(data, end=" ")