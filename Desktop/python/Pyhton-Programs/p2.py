first_name ="Bro"
food = "pizza"

print(f"hello {first_name}")
print (f"do u like {food}?")
#That f before the string is short for formatted string literal — we just call it f-string in Python
#It lets you embed variables or expressions directly into your strings by using {} brackets.

#No need for .format() or messy string concatenation like "Hello " + name.
# This will look for the value of first_name (which is "Bro") and insert it into the string.


#program 02

#string + variables

city = "Dhaka"
print(f"My city is  {city}")

#integer

age = 21

print(f"I am {age} years old")

#float

price = 3.89 

print(f"The price of this {food} is {price} dollars")