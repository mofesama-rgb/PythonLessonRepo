mathematics = 75
english = 82
geography = 68
science = 91
psychology = 84

print("Mathematics:", mathematics)
print("English:", english)
print("Geography:", geography)
print("Science:", science)
print("Psychology:", psychology)

total_grade = mathematics + english + geography + science + psychology
average_score = total_grade / 5

report = f"My grades are as follows. My Mathematics is {mathematics}, my English is {english}, \
my Geography is {geography}, my Science is {science}, and my Psychology is {psychology}. \
The total grade is: {total_grade}, and the average score is: {average_score}"
print(report)