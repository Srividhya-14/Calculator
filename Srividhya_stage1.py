# Stage 1: Basic Calculator
user_input = input("Input: ")
num1_str, num2_str, operator = user_input.split(",")

num1 = float(num1_str.strip())
num2 = float(num2_str.strip())
operator = operator.strip()

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2

if operator in ['+', '-', '*'] or (operator == '/' and num2 != 0):
    print(f"Result = {int(result) if result == int(result) else result}")
