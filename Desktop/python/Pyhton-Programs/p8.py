#logical operators
# and, or, not -- 1. or = True if at least one operand is True
# 2. and = True if both operands are True
# 3. not = True if the operand is False

# Python program to demonstrate logical operators

operator = input("Enter operator (and, or, not): ")

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

if operator == 'and':
    result = (num1 and num2)
    print(f"{num1} and {num2} = {result}")
elif operator == 'or':
    result = (num1 or num2)
    print(f"{num1} or {num2} = {result}")