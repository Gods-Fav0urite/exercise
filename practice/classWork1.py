greeting = "Hello"
name = "God's Favourite"
age = 29

# PRINTING VARIABLES TYPES
print(type(greeting))
print(type(age))
print(type(name))

# ADDING VARIABLES AND STRING TOGETHER
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# ADDING TWO STRING VARIABLES TOGETHER
print(greeting + name)

# ADDING TWO NUMBER VARIABLES TOGETHER
print(age + 10)
b = 10
c = age / b
print("The division solution is: " + str(c))

# INCREMENTING AND DECREMENTING VARIABLES
age += 1
print("I am now " + str(age) + " years old.")
age -= 1
print("I am now " + str(age) + " years old.")

# USING AVRIABLE IN AN IF STATEMENT
print("I am " + str(age) + " years old.")
if age != 30 and age < 30:
    print("I am not 30 years old yet.")
else:
    print("I am 30 years old.")


# IF STATEMENT EXAMPLE: BUILDING A DICE ROLLING SIMULATION 
from random import randint as random
dice = random(1,6)
print("You rolled a " + str(dice))
if dice == 6:
    print("You got 6!")
elif dice == 5:
    print("You got 5!")
else:
    print("Try again")

# IMPORTING THE RANDOM MODULE AND GENERATING A RANDOM PERCENTAGE
import random
random_percent = random.random() * 100
print(f"The random percentage is: {random_percent:.2f}")  # Generates a random float between 0.0 and 1.0

# NESTED IF STATEMENT EXAMPLE: CHECKING IF A PERSON IS AN ADULT BASED ON AGE
age = 32
print("Age: " + str(age))
if age > 20:
    print("You are an adult.")
elif age >= 20:
    print("You are a teenage.")
    if age >= 10:
        print("You are a child.")
else:
    print("You are a child.")