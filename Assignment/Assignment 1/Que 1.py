# program to check percentage of students

m1 = float(input("Enter marks of subject 1:"))
m2 = float(input("Enter marks of subject 2:"))
m3 = float(input("Enter marks of subject 3:"))
m4 = float(input("Enter marks of subject 4:"))
m5 = float(input("Enter marks of subject 5:"))

gain_marks = m1 + m2 + m3 + m4 + m5

perc = (gain_marks / 500) * 100

print("Percentage of five subject:",perc)