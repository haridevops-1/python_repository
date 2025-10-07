#  Question 1
# A cinema charges:
# ₹150 for ages under 18
# ₹250 for ages 18–60
# ₹100 for ages above 60

# def input (n):
#     if n < 18:
#         print("150")
#     elif n >= 18 and n <= 60:
#         print("250")
#     elif n > 60:
#         print(100)
#     else:
#         print("Invalid Input")
# input(12)
# input(56)
# input(76)

# Question 2
# Stadium ticket rules:
# age < 12 → ₹50
# age 12–59 → ₹120
# age ≥ 60 → ₹80
# If age is even, ₹5 discount.
# def give_input(age):
#     if age < 12:
#         t = 50
#     elif age >= 12 and age <= 59:
#         t = 120
#     elif age >= 60:
#         t = 80
#     else:
#         print("invalid input")
#     if age % 2 == 0:
#         t -=5
#     print(t)
# give_input(11)
# give_input(42)
# give_input(68)
# give_input(21)
# A shopkeeper has n mangoes.
# Each basket holds 5 mangoes.
# Find:
# Full baskets
# Leftover mangoes
# def mangoes(m):
#     Full_baskets = m //5
#     print("you took", Full_baskets)
#     left_over = m % 5
#     print("you left_over", left_over)
# mangoes(50)
# mangoes(37)
# A child has n candies and eats one candy per day.
# Print how many are left each day.
def candies (m):
    for i in range(1, m +1):
        l = m -i
        print("day",i, "=", "candies_left", l)
candies(5)
candies(10)
candies(3)
# An employee gets bonus on sales:
# ≥100 units → 10% bonus
# 50–99 units → 5% bonus
# <50 → no bonus
# Input: Salary and sales
# Output: Bonus and Total Salary

# salary = int(input("enter your salary: "))
# sales = int(input("enter you sales: "))
# bonus = 0
# if sales >= 100:
#     t = salary * 0.10 
#     print (t + salary)
# elif sales >50 and sales <=99:
#     t = salary * 0.5
#     print(t + salary)
# elif sales < 50:
#     print("no bonus")
# else:
#     print("Invalid Input")


# Earnings of a Salesperson:
# ≤ ₹5000 → 5% commission
# ₹5001–₹10000 → 10%
# ₹10000 → 15%
# 7000 → 700  
# 12000 → 1800  
# 11000 → 1650
# def num(n):
#     if n <=5000:
#         c=n*0.05
#     elif n <10000 and n >=5001:
#         c=n*0.10
#     elif n >= 10000:
#         c=n*0.15
#     print(int(c))
# num(7000)
# num(12000)
# num(11000)

# Question 7
# Shopping Discount:
# Price > 100 → 10% off
# Price 50–100 → 5% off
# Price <50 → no discount
# 200 → 180  
# 80 → 76  
# 40 → 40  
# 150 → 135
# def num(n):
#     if n > 100:
#         d=(n*0.10)
#     elif n >= 50:
#         d=(n*0.5)
#     elif n < 50:
#         d=0
#     f=n-d
#     print(int(f))
# num(200)
# num(80)
# num(40)
# num(150)

# Taxi Charges:
# First 10 km → ₹15/km
# Next 20 km → ₹12/km
# Beyond 30 km → ₹10/km
# 15 → 180  
# 35 → 350  
# 10 → 150
# def num(n):
#     if n <= 10:
#         print(n*15)
#     elif n <=20:
#         print(n*12)
#     else:
#         print(n*10)
# num(15)
# num(35)
# num(10)
# num(31)

# # Lily's Birthday Gifts:
# Odd birthdays → 1 toy
# Even birthdays → money (₹10, ₹20, ₹30, …)
# 10
# 5
# 150.00
# def lily_gifts(n):
#     toys = 0
#     money = 0
#     amount = 10

#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             toys += 1
#         else:
#             money += amount
#             amount += 10

#     print(toys)
#     print(money)
# lily_gifts(10)










######

#  def num(a,b):
#     for i in range (a,b+1):
#         print(i)
# num(10,20)

# def count(a,b,n):
#     total=0
#     for i in range(a,b+1):
#         if i % 2 == 0:
#             total=total+1
#     print(total)
#     if n == 0:
#         print("invalid")

# count(10,20,2)
# count(10,15,2)
# count(10,10,2)
# count(10,20,0)

# def count(a,b,n):
#     total = 0
#     if n > 0:
#         for i in range(a,b+1):
#             if i % 2 == 0:
#                 total=total+1
#         print(total)
#     else:
#         print("invalid")
# count(10,20,2)
# count(10,15,2)
# count(10,10,2)
# count(10,20,0)
# count(10,20,-1)

# def steps(a):
#     if a < 1000:
#         print('you dont have any points')
#     else:
#         if a >= 1000 and a <5000:
#             b = (a // 1000)*5
#             print(b)
#         elif a >= 5000:
#             d=(a // 1000)*5
#             bonus=(a//5000)*20
#             total=d+bonus
#             print(total)
# steps(4000)
# steps(2000)
# steps(6000)
# steps(13000)
# steps(20000)
# steps(500)