# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 14:
# Print a downward Half-Pyramid Pattern of Star (asterisk)

# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# use loop and range
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\t")