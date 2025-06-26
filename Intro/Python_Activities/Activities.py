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

#Activity 04: Coin Toss
""" You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads. There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails. """

import random
toss = random.randint(0, 1)  # Generate a random number, either 0 or 1
if toss == 0:
    print("Heads")
else:
    print("Tails")


for i in range(10):
    toss = random.randint(0, 1)  # Generate a random number, either 0 or 1
    if toss == 0:
        print("Heads")
    else:
        print("Tails")

import random

max_throws = 100
for throw in range(1, max_throws + 1):
    result = random.randint(0, 1)  # 0 for Tails, 1 for Heads
    side = "Heads" if result == 1 else "Tails"
    print(f"Throw {throw}: {side}")
    if result == 1:
        print(f"Heads appeared on throw number {throw}")
        break
else:
    print("Heads never appeared in 100 throws.")


#Activity 05: Collatz Conjecture
""" The Collatz conjecture is a sequence defined as follows: start with any positive integer n. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat the process indefinitely. The conjecture states that no matter what number you start with, you will always eventually reach 1."""
n= int(input("Enter a positive integer to start: "))
count = 0  # Initialize a counter to keep track of the number of steps
print("Collatz sequence:")
while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = n // 2  # If n is even, divide it by 2
    else:
        n = 3 * n + 1  # If n is odd, multiply by 3 and add 1
    count += 1  # Increment the step counter
print(n)  # Print the final value, which should be 1
print(f"Total steps taken to reach 1: {count}")














