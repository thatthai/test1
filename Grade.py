#input
thai = float(input())
math = float(input())
english = float(input())
science = float(input())
sport = float(input())

#process gpa
gpa = (thai + math + english + science + sport)/5

#output
print("THAI = " + str(thai))
print("MATH = " + str(math))
print("ENGLISH = " + str(english))
print("SCIENCE = " + str(science))
print("SPORT = " + str(sport))
print("---")
print("GPA = " + str(gpa))