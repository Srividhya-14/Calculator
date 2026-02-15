# Stage 3: Student Grade Calculator
user_input = input("Input: ")
name, mark1_str, mark2_str, mark3_str = user_input.split(",")

name = name.strip()
mark1 = float(mark1_str.strip())
mark2 = float(mark2_str.strip())
mark3 = float(mark3_str.strip())

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
else:
    grade = 'F'

print(name)
print(f"Total: {int(total)}/300")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
