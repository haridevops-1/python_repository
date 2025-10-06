# n = int (input("enter your marks: "))
# if n >= 75:
#     print("A Grade")
# elif n >= 60 and n < 75:
#     print ("B grade")
# elif n>=45 and n> 60:
#     print(" C Grade") 
# elif n< 45:
#     print("D Grade")
# else:
    # print("INvalid Input")

# num = int(input("enter your number:"))
# if num %2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# Let a be a year, write a program to check whether this year is a leap year or not.

 

# Print "Y" if it's a leap year and "N" if it's a common year.

 

# The rule for determining a leap year is:

# The year must be divisible by 4.

# However, if the year is also divisible by 100, it is not a leap year unless...

# The year is also divisible by 400, in which case it is a leap year.

# For example:

# The year 2000 was a leap year because it is divisible by 400.

# The year 1900 was not a leap year because it is divisible by 100 but not by 400.

# The year 2020 was a leap year because it is divisible by 4 but not by 100
    # def is_leap_year(a):
    # if ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0):
    #     print("Y")
    # else:
    #     print("N")


# i = 0
# for i in range (0, 12, +1): 
#     print(i)
# i = 0
# while i < 12:
#     i +=1   
#     print(i) 


### Print numbers from 1 to 10 using a while loop.
# i = 1
# while i<10:
#     print(i)
#     i +=1

###Find the sum of numbers from 1 to 50 using a while loop.
# i = 1
# total = 0
# while i <= 50:
#     total = total + i 
#     i +=1
   
# print("sum of =", total)

###Find the sum of all even numbers between 1 and 100
# i = 0
# sum = 0
# while i < 100:
#     if i % 2 == 0:
#         sum += i
#         i +=1
print("total", sum)
n = 5
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum of first", n, "natural numbers is", total)

