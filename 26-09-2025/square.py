### Input a number of 'n' and print all power of 2 upto 2 power n using a "while or or loop"

##while loop
n = int(input("Enter your value to find:"))
a = 1
b =2
while a< n:
    print(b)
    b = b *2
    a = a+1


### Write a program that prints the square of numbers from 1 to 10 using a while loop

## while loop
a=1
b=10
while a<b:
    print(a **2)
    a= a+1

### for loop
for i in range(1,11):
    print(i **2)
    i = i+1