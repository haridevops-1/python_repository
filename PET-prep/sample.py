# Question 1:
# A cinema charges: # * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60
# Write a program that asks for age and prints the ticket price.
# Sample Input:
# 65
# Sample Output:
# 100

# n = int(input("Enter your age: "))
# if n < 18:
#     print("your ticket price is $150")
# elif n > 18 and n < 60:
#     print("Your ticket price is $250")
# elif n > 60:
#     print("Your ticket price is $100")
# else:
#     print("Invalid Input")

##### Question 2:
# A stadium sells entry passes with the following rules:
# * If age < 12 → Ticket = ₹50
# * If age between 12–59 → Ticket = ₹120
# * If age ≥ 60 → Ticket = ₹80
# Additionally, if the person’s age is a Even number, give a ₹5 discount.
# Get the input from the user and return the final discounted stadium ticket price.


age = int (input("ENter your age: "))


if age < 12:
    print("50")
    if age % 2 == 0:
        discount = discount - 5
        print(discount)
elif age <= 12 and age < 59:
    print("120")
elif age >= 60 :
    print(60)
else:
    print("INvalid")



# Question 3: A shopkeeper has n mangoes. He wants to pack them into baskets, with 5 mangoes in each basket. 
# Write a program to calculate: * How many full baskets can be made * How many mangoes will be left 
# Sample Input: 23 Sample Output: Full Basket is 4 Left Over mangoes is 3.

# Mango Basket Calculation
# num = int(input("Enter your having mangoes: "))
# full_basket = num //5
# print("The full basket taken is:", full_basket)
# Left_over = num % 2
# print("The left_over is:", Left_over)

# Question 4: A child has n candies and eats one candy each day until all are finished. 
# Write Python program to print how many candies the child ate and how many are left each day. 
# Sample Input: 3 Sample Output: Day 1 = 2 left Day 2 = 1 left Day 3 = 0 left

# Candies eaten each day
# candy = int(input("Enter your candies:"))
# for day in range (1, candy +1):
#     left = day - candy
#     print("Day", day, "=", "left", left)
# Question 5: An employee gets a monthly salary. * If sales ≥ 100 units → bonus = 10% * 50–99 units → bonus = 5% * <50 → no bonus Write a program that asks for salary and sales and prints total salary including bonus. 
# Sample Input: Enter your salary 40000 Enter your sales 120 
# Sample Output: Bonus = 4000 Total Salary = 44000

# Employee Bonus Calculation
# salary = int(input("Enter your salary: "))
# sales = int(input("Enter your sales: "))

# if sales >= 100:
#     bonus = salary * 0.10
# elif sales >= 50:
#     bonus = salary * 0.05
# else:
#     bonus = 0

# total = salary + bonus

# print("Bonus =", int(bonus))
# print("Total Salary =", int(total))

# Question 6: Earnings of a Salesperson: * 5% commission for sales ≤ ₹5000 * 10% for sales 5001–10000 * 15% for sales > 10000 
# Input weekly sales of the salesperson and calculate commission. Test Cases with their 
# output: 7000 -> 700 12000 -> 1800 11000 -> 1650

# Salesperson Commission
# sales = int(input("Enter weekly sales amount: "))

# if sales <= 5000:
#     commission = sales * 0.05
# elif sales <= 10000:
#     commission = sales * 0.10
# else:
#     commission = sales * 0.15

# print(int(commission))


# Multi-Item Shopping Discount * Price > 100 → 10% discount * Price 50–100 → 5% discount * Price <50 → no discount 
# Print discounted price per item Test cases with their 
# output: 200 → 180 80 → 76 40 → 40 150 → 135

# Shopping Discount
# price = int(input("Enter item price: "))

# if price > 100:
#     discounted = price * 0.9
# elif price >= 50:
#     discounted = price * 0.95
# else:
#     discounted = price

# print(int(discounted))


# Question 8: A file manager needs to classify files based on their extension. .csv → 
# print output as "This is an Excel File" .jpg → print output as "This is a JPEG File" .doc → print output as "This is a Word File" .pdf → print output as "This is a PDF File" .py → print output as "This is a Python File" .Any other input, print output as "Unknown File Type" Print the result based on the input Sample Input: .csv Sample Output: This is an Excel file Sample input: .py 
# Sample Output: This is a Python File

# File Type Checker
# file = input("Enter file extension: ")

# if file == ".csv":
#     print("This is an Excel File")
# elif file == ".jpg":
#     print("This is a JPEG File")
# elif file == ".doc":
#     print("This is a Word File")
# elif file == ".pdf":
#     print("This is a PDF File")
# elif file == ".py":
#     print("This is a Python File")
# else:
#     print("Unknown File Type")

# Question 9: Taxi charges: * First 10 km → ₹15/km * Next 20 km → ₹12/km * Beyond 30 km → ₹10/km 
# Estimate the Taxi charges based on the input and print the output.
# Sample Input: 15 → 180 35 → 350 10 → 150
# Taxi Fare Estimation
# km = int(input("Enter total km: "))

# if km <= 10:
#     fare = km * 15
# elif km <= 30:
#     fare = (10 * 15) + (km - 10) * 12
# else:
#     fare = (10 * 15) + (20 * 12) + (km - 30) * 10

# print(fare)


# Question 10: Lily is N years old. On every odd birthday (1, 3, 5, …) → she gets 1 toy. 
# On every even birthday (2, 4, 6, …) → she gets money. The money starts at ₹10 on her 2nd birthday. 
# On each next even birthday, it increases by ₹10 more: 2nd birthday → ₹10 4th birthday → ₹20 6th birthday → ₹30 and so on. At the end, print the following: * Number of toys Lily has. 
# * Total money she has (money from even birthdays after brother takes ₹1). Input * Lily’s age (N) * Nothing else (price of toys is not needed because we are not selling) 
# Output * Number of toys * Total money (formatted with 2 decimal places) Sample TestCase: Input 10 Output 5 150.00 Explanation: Toys → 1,3,5,7,9 → 5 toys. 
# Money → 10 + 20 + 30 + 40 + 50 = ₹150. 
# Lily Birthday Gifts
# N = int(input("Enter Lily's age: "))

# toys = 0
# money = 0

# for i in range(1, N + 1):
#     if i % 2 == 1:   # Odd birthday → toy
#         toys += 1
#     else:             # Even birthday → money increases ₹10 each time
#         money += (i // 2) * 10

# print(toys)
# print(f"{money:.2f}")
