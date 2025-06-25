# Activity 01: Basic Input and Output
my_name = input("Enter your name: ")
my_age = int(input("Enter your age: "))  # Convert input to integer
print(f"Hello {my_name}, I am {my_age} years old.")

my_age = my_age + 1  # Now this works because my_age is an integer
print(f"Next year, I will be {my_age} years old.")

favorite_color = input("What is your favorite color? ")
print(f"Hello {my_name}, you are {my_age} years old and your favorite color is {favorite_color}.")

# Activity 02: Raindrops
""" Your task is to convert a number into a string representing sounds of raindrops based on its potential factors. A factor is a number that divides another number evenly, without leaving a remainder. The simplest way to check if a number is a factor of another is by using the modulo operation.

The rules for raindrops are as follows: if a given number:

has 3 as a factor, add "Pling" to the result.
has 5 as a factor, add "Plang" to the result.
has 7 as a factor, add "Plong" to the result.
has none of 3, 5, or 7 as factors, the result should be the digits of the number itself.
Examples:

28 has 7 as a factor, but not 3 or 5, so the result would be "Plong."
30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang."
34 is not divisible by 3, 5, or 7, so the result would be "34." """
    # Activity 02: Raindrops - Basic Version
x=int(input("Enter a number to convert to raindrop sounds: "))
result = ""
if x % 3 == 0:
    result += "Pling"
if x % 5 == 0:
    result += "Plang"
if x % 7 == 0:
    result += "Plong"
if result == "":
    result = str(x)  # Convert number to string if no factors found
print(f"The raindrop sounds for {x} is: {result}")

    # Activity 02: Raindrops - Alternative Version
x=int(input("Enter a number to convert to raindrop sounds: "))
result = ("Pling" if x % 3 == 0 else "") + \
         ("Plang" if x % 5 == 0 else "") + \
         ("Plong" if x % 7 == 0 else "")
print(f"The raindrop sounds for {x} is: {result or str(x)}")

# Activity 03: Count Occurrences
    #Activity 03: Count Occurrences - Basic Version
"""calculate the number of occurrences of the letter 'o' in the string "welcome to gomycode" """
count = 0
text = "welcome to gomycode"
for char in text:
    if char == 'o':
        count = count +1
print(f"The letter 'o' occurs {count} times in the string '{text}'.")

    # Activity 03: Count Occurrences - Alternative Version
text = "welcome to gomycode"
count = text.count('o')
print(f"The letter 'o' occurs {count} times in the string '{text}'.")






