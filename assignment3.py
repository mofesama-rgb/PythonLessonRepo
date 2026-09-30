#1 (Prime Factorization) A prime number is divisible only by itself and 1 (e.g., 2, 3, 5,
# 7, 11, 13, …). The prime factors of a number are a set of prime numbers that multiply to
# gether to result in the given number. Thus, if a number is a divider of the given number
# and also a prime number, it is a prime factor of the given number. Prime factorization is
# the search for all prime factors of a given number. Write a script that uses a trial and error
# approach to determine the prime factors of the number 1537.

number = int(input("Enter a number: "))

factor = 2

print(f"Prime factors of {number}:")

while factor <= number:
    if number % factor == 0:
        print(factor)
        number = number // factor
    else:
        factor += 1

#2 (Rabbit Births) A farmer wants to keep track of the average number of rabbits born
# on his farm every month. He records the number of does (female rabbits) he has combined
# with the number rabbits born every month. Develop a sentinel-controlled-repetition
# script that prompts the user to input the number of does living in the farm and the number
# of rabbits born in a specific month. After processing all input information, the script
# should calculate and display the combined average number of rabbits born per doe.

# total_rabbits = 0
# total_does = 0

# does = int(input("\nEnter number of does (-1 to stop): "))

# while does != -1:
#     rabbits = int(input("Enter number of rabbits born: "))

#     total_rabbits += rabbits
#     total_does += does

#     does = int(input("\nEnter number of does (-1 to stop): "))

# if total_does > 0:
#     average = total_rabbits / total_does
#     print(f"Combined average number of rabbits born per doe: {average:.2f}")
# else:
#     print("No rabbit data was entered.")


#3 (Challenge: Fibonacci Sequence) In the Fibonacci sequence, each number is the
# sum of the two preceding ones. The first 10 Fibonacci numbers are as follows:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
# Write a script where a user inputs a position (a number) and the number in that position
# in the Fibonacci Sequence is displayed.


position = int(input("\nEnter the Fibonacci position: "))

first = 0
second = 1

if position == 0:
    result = first

elif position == 1:
    result = second

else:
    for number in range(2, position + 1):
        result = first + second
        first = second
        second = result

print(f"The Fibonacci number at position {position} is {result}")