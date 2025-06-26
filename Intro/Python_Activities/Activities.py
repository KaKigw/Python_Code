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

# Activity 06: List Operations
""" Define the list: list = [17, 38, 10, 25, 72], then perform the following actions:

Sort and display the list
Add the element 12 to the list and display the list
Reverse and display the list
Display the index of the element 17
Remove the element 38 and display the list
Display the sublist from the 2nd to the 3rd element
Display the sublist from the beginning to the 2nd element
Display the sublist from the 3rd element to the end of the list
Display the complete sublist of the list
Display the last element using negative indexing. """

my_list = [17, 38, 10, 25, 72]
my_list = sorted(my_list)  # Sort the list
print(f"Sorted list: {my_list}")

my_list.append(12)  # Add the element 12 to the list
print(f"List after adding 12: {my_list}")

my_list.reverse()  # Reverse the list
print(f"Reversed list: {my_list}")

my_list.sort(reverse=True)  # Sort the list again to maintain order
print(f"List after sorting in descending order: {my_list}")

index_of_17 = my_list.index(17)  # Display the index of the element 17
print(f"Index of 17: {index_of_17}")

index_of_38 = my_list.pop(my_list.index(38))  # Remove the element 38 and display the list
print(f"List after removing 38: {my_list}")

my_list.remove(38)  # Remove the element 38
print(f"List after removing 38: {my_list}")

print(f"Sublist from 2nd to 3rd element: {my_list[1:3]}")
print(f"Sublist from beginning to 2nd element: {my_list[:2]}")
print(f"Sublist from 3rd element to end: {my_list[2:]}")
print(f"Complete sublist: {my_list[:]}")
print(f"Last element using negative indexing: {my_list[-1]}")

# Activity 07: Dice Throwing
""" Throw 2 dices sum the results and display the result and the number of times the result was obtained in 100 throws and display it in a dictionary """
import random
dice_results = {}
for _ in range(100):
    die1 = random.randint(1, 6)  # Simulate the first die
    die2 = random.randint(1, 6)  # Simulate the second die
    result = die1 + die2  # Calculate the sum of the two dice
    if result in dice_results:
        dice_results[result] += 1  # Increment the count for this result
    else:
        dice_results[result] = 1  # Initialize the count for this result
print("Dice results after 100 throws:")
for result, count in dice_results.items():
    print(f"Result {result}: {count} times")


#activity 08: Student Dictionary
""" Create a dictionary named student with the following keys and values:

  name: "Alice"
  age: 21
  major: "Data Science"
Access and print the value associated with the key name.
Print all the keys in the dictionary.
Print all the values in the dictionary.
Update the age to 22.
Add a new key-value pair: graduation_year: 2025.
Print the updated dictionary. """
student = {
    "name": "Alice",
    "age": 21,
    "major": "Data Science"
}
print("Name:", student["name"])  # Access and print the value associated with the key name
print(f"Keys in the dictionary: {student.keys()}")  # Print all the keys in the dictionary
print(f"Values in the dictionary: {student.values()}")  # Print all the values in the dictionary
student["age"] = 22  # Update the age
student["graduation_year"] = 2025  # Add a new key-value pair
print(f"Updated dictionary: {student}")  # Print the updated dictionary

# Activity 09: Set Operations
""" Create two sets: set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 7, 8}.
Compute and print the union of set1 and set2.
Compute and print the intersection of set1 and set2.
Compute and print the difference between set1 and set2.
Compute and print the symmetric difference between set1 and set2. """
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Union of set1 and set2: {set1 | set2}")
print(f"Intersection of set1 and set2: {set1 & set2}")
print(f"Difference between set1 and set2: {set1 - set2}")
print(f"Symmetric difference between set1 and set2: {set1 ^ set2}")

# Activity 10: Modify Tuple
""" Write a Python script to modify a tuple by adding an element at the end of it.

For inputs with tuple (1, 2, 3) and element 4, the return value should be (1, 2, 3, 4).
Hint: You need to first convert the tuple to another data type, such as a list. """
my_tuple = (1, 2, 3)
element_to_add = 4
# Convert the tuple to a list, add the element, and convert it back to a tuple  
my_list = list(my_tuple)  # Convert tuple to list
my_list.append(element_to_add)  # Add the element to the list
my_tuple = tuple(my_list)  # Convert the list back to a tuple
print(f"Modified tuple: {my_tuple}")  # Print the modified tuple

