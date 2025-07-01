#input() = A function that prompts the user to enter data returns the entered data as a string

name = input("what is your name?: ")
age = input("what is your age?: ")

print(f"hello {name}")
print(f"You are {age} years old!")

age= int(age)+1
print(f"Next year you will be {age} years old!")