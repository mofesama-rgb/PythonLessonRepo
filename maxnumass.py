# numb1 = int(input("Enter first number: "))

# numb2 = int(input("Enter second number: "))

# numb3 = int(input("Enter third number: "))

# max_numb = numb1

# if numb2 > max_numb:

#     max_numb = numb2

# if numb3 > max_numb:

#     max_numb = numb3

# print(max_numb)
# print(min(numb1, numb2, numb3))
# print(max(numb1, numb2, numb3))

# grade = 85
# if grade >= 60:
#     print("Pass")
# if 1:
#     print("Non zero values are true")
# if 0:
    # print("Zero is false")
# grade = 77
# if grade >= 60:
#     print("Pass")
# else:
#     print("Fail")
#     print("You must retake this course")
# if grade >= 60:
#     result = "passed"
# else:
#     result = "failed"
# result = "passed" if grade >= 60 else "failed"
# print(result)
# print("passed" if grade >= 60 else "failed")
# if grade >= 60:
#     print("Pass")
# else:
#     print("Fail")
# print("You must retake this course")
# grade = 96
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")

# product = 3
# while product <= 50:
#     # product = product*3
#     product *= 3
#     print(f"inner print {product}")
# print(product)

# product = 7
# while product <= 1000:
#     product *= 7
#     print(product)

# for character in "mofe":
#     # print(character, end="  ")
#     print(character)
# print(10, 20, 30, sep="  ")
# print(10, 20, 30, )

# total = 0
# for number in [2, -3, 0, 17, 9]:
#     total = total + number
# print(total)

# for counter in range(0, 200, 5):
#     print(counter, end="  ")

# total = 0
# for counter in range(1, 8):
    # print(counter, end="  ")
    # total += counter
# variable = 12
# variable **= 2
# print(variable)

# total = 0
# grade_counter = 0
# grades = [55, 63, 76, 90, 84, 43, 88, 74, 67, 98]

# for score in grades:
#     # print(score)
#     total += score
#     grade_counter += 1
# average = total / grade_counter
# print(f"The class average is {average}")
# example1, example2 = 32, 44
# print(f"{example1} times {example2} is {example1 * example2}")

"""class average program with sentinel-controlled iteration"""
# initialization phase
total, grade_counter = 0, 0

# processing phase
grade = int(input("Enter grade, any number outside range 0-100 will end code: "))
while grade in range(0, 101):
# while grade != -1:
    total += grade
    grade_counter += 1
    print(f"this is the total: {total}, and youve inputed a value {grade_counter} times")
    grade = int(input("Enter grade, any number outside range 0-100 will end code: "))

# termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f"Class average is {average:.2f}")
else:
    print("No grades entered")