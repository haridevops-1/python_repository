# a = int (input("Enter the marks to find Grade:"))
# match a:
#     case a if a >= 80 and a <= 100:
#         print("Your Grade is A")
#     case a if a >= 60 and a <= 79: 
#         print("Your Grade is B")
#     case a if a >= 50 and a  <=59:
#         print("Your Grade is C")
#     case a if a >= 40 and a <= 49:
#         print("Your Grade is D")
#     case a if a<40:
#         print("fail")
#     case _:
#         print("Invalid Input")

#Finding vowels using OR conditional operator

# x = input(" Enter your Alphabets: ")
# match x:
#     case "a"| "e" | "i" | "o" | "u":
#         print("vowels")
#     case _:
#         print("not vowels")

# finding age  using if / else condition:

# age = int (input("Enter your age: "))
# if age <= 5:
#     print("free")
# elif age >= 5 and age <= 12:
#     print("10")
# elif age >= 13 and age <= 64:
#     print("20")
# elif age >= 65:
#     print("15")
# else:
#     print("Invalid Input")

#finding month
month = int(input("Enter your number to find: "))
match month :
    case 1 :
        print("january")
    case 2 :
        print("february")
    case 3 :
        print("March")
    case 4:
        print("April")
    case 5:
      print("May")
    case 6:
       print("June")
    case 7:
      print("july")
    case 8:
       print("August")
    case 9:
        print("september")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print ("December")
    case _:
        print("Invalid Input")