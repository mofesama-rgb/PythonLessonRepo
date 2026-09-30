# 'this is my first string class'
# print("This is my \"first string\" class")
# print('It\'s my birthday, I\'m 12 years old')
# print('It\'s my birthday, \nI\'m 12 years old')
# print('\tIt\'s my birthday, \nI\'m 12 years old')
my_first_variable = "hello"
# print(my_first_variable)
FAV_FOOD = "pizza"
_private_variable = "age"
var_1 = 40
maths_grade = 80
english_grade = 67
name = "moffettf"


# string concatenation
# print(my_first_variable.strip() + " " + FAV_FOOD)
# new_word = _private_variable + " = " + str(var_1)
# print(new_word)


# string format
# print(f"My {_private_variable} is {var_1} ")
# report = f"My name is {name}, i got {english_grade} in english and {maths_grade} in mathematics. \
# My total grade is {maths_grade + english_grade}"
# print(report)
# print(type(name))

name2 = "to be or not to be, tommorrow will be a good day"
# string method
# print(name.capitalize())
# print(name.upper())
# print(name.count("f", 3, 8))
# print(name2.count("be"))
print(name2.find("be"))
print(name2.find("to", 15, 25))
print(len(name2))
print(name2[47])
year = int(input("please enter year of birth for age: "))
current_year = 2026
age = current_year - year
# print("your age is:", age)
print(f"your age is {age}")
name.isalnum