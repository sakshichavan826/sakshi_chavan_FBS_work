# Program to input 5 subject marks and display grade

# Taking 5 subject marks from the user
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5


if percentage >= 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Class"
elif percentage >= 50:
    grade = "Second Class"
elif percentage >= 35:
    grade = "Pass Class"
else:
    grade = "Fail"

print(f"\nTotal Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")