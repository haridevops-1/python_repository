a = 10
b = 20
print(a, b)


# for finding the leap yaer or not
n = int(input("Enter your year: "))
print(n)
if n % 4 == 0:
    print("It's leap year")
else:
    print("not leap year")

# For divisible by 3 or 5

n = int(input("Enter the number you want: "))
print(n)

if n % 3 == 0 or n % 5 == 0:
    print("It is Divisble by 3 or 5")
else:
    print("It is not Divisible by 3 or 5")

# for finding the 21 century(2001 to 2100 )
n = int(input("Enter the year to find the 21 century: "))
print(n)
if n >= 2001 and n <= 2100:
    print("This year is 21 century")
else:
    print("This is not 21 century")
