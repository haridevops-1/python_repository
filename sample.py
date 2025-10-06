# Question 1:
# A cinema charges: # * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60
# Write a program that asks for age and prints the ticket price.
# Sample Input:
# 65
# Sample Output:
# 100

n = int(input("Enter your age: "))
if n < 18:
    print("your ticket price is $150")
elif n > 18 and n < 60:
    print("Your ticket price is $250")
elif n > 60:
    print("Your ticket price is $100")
else:
    print("Invalid Input")