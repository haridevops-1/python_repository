### finding datatype and variable

# Question-1: Create a variable called age and store your age in it.
# Then print the value of age.

# age = 70
# print(age)

# Question-2: Create a variable and check its data type using type()
# X = 10.09
# print("the type of x:", type(X))

# Question-3: Add two numbers and print the result

# a = 5
# b = 7
# result = a +b
# print(result )

## Question-4: Create variables with different data types and print their types

# a = 6
# b = "hari"
# c = 3.14
# d = True

# print("a", type(a))
# print("b", type(b))
# print("c", type(c))
# print("d", type(d))

## Question-5: Take age as input from user and print the type

# n= int(input("enter you age: "))
# print("n", type(n))

#### IF /ELSE LOOP

# Question 1: Positive or Negative

# Ask the user to enter a number.
# Check if it is positive, negative, or zero, and print a message.

# n = int(input("enter your number:"))

# if n > 0:
#     print("positive")
# elif n < 0:
#     print("negative")
# else:
#     print("Invalid Input")

# Question 2: Even or Odd

# Ask the user to enter a number.
# Check if it is even or odd using if-else.

# n = int(input("enter your value: "))
# n = int(input("Enter your number: "))

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Question 3: Age Check

# Ask the user to enter their age.
# If age is 18 or above, print "You are an adult."
# Else, print "You are a minor."

# n = int(input("enter your age: "))

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# Question 4: Find the Largest Number

# Take three numbers from the user.
# Use if-elif-else to find and print the largest number.
# Take input

# n = int(input("Enter first number: "))
# m = int(input("Enter second number: "))
# o = int(input("Enter third number: "))

# Compare
# if n >= m and n >= o:
#     print("The largest number is:", n)
# elif m >= n and m >= o:
#     print("The largest number is:", m)
# else:
#     print("The largest number is:", o)


## Question 5: Pass or Fail

# Ask the user to enter their marks out of 100.
# If marks are greater than or equal to 40, print "You passed."
# Otherwise, print "You failed."

# marks = int(input("Enter your marks (out of 100): "))

# if marks > 100 or marks < 0:
#     print("Invalid input. Marks should be between 0 and 100.")
# elif marks >= 40:
#     print("You passed.")
# else:
#     print("You failed.")


### WHILE LOOP CONCEPT

# Q1. Print Multiplication Table of a Number

# 🔹 Ask user to enter a number
# 🔹 Print its multiplication table from 1 to 10 using while loop
# n = int(input("enter the number to multiply: "))
# i = 1
# while i<=10:
#     print(i * n)
#     i +=1

# Q2. Reverse a Number

# 🔹 Input: 123 → Output: 321
# 🔹 Use while loop to reverse the digits of the number

n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10         # Get the last digit
    rev = rev * 10 + digit # Add it to reversed number
    n = n // 10            # Remove the last digit

print("Reversed number is:", rev)
