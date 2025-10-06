#1st problem
# N = int(input("Enter your first value:"))
# M = int (input("Enter your second value: "))
# O = N + M
# if O %2 ==0:
#     print("Even")
# else:
#     print("Odd")

#2nd problem
# a = input("Enter the stream to grab: ")
# b = input("Enter your Stream:")
# c = input ("Enter your stream: ")
# a = input("Enter your Stream: (science, Commerce, Arts: )")
# match a:
#     case 'science':
#         b = input("Enter a sub-choice:")
#         match b:
#             case 'Medical':
#                 print("You chose sub-choice as science-Medical")
#             case 'Engineering':
#                 print("You chosen sub-choice as Science- Engineering")
#             case _:
#                 print("Invalid Input")
#     case 'Commerce':
#         c = input("Enter your Sub-course")
#         match c:
#             case 'CA':
#                 print("You chosen Commerc- CA")
#             case 'B com':
#                 print("You chose sub-choice as commerce-B com")
#             case _:
#                 print("Invalid Input")
#     case 'Arts':
#         d = input("Enter your sub-choice:")
#         match d:
#             case 'History':
#                  print("you chosen sub-choice as Arts - History")
#             case 'Literature':
#                  print("You chosen Sub-choice as Arts- Literature") 
#             case _:
#                 print("Invald Input")
#     case  _:
#         print("Invalid input")

##9th problem
# a = int(input("Enter the A value in Kilometer : "))
# b = int(input("enter the number 1 for (meter) 2 for (Centimeter) 3 for (millimeter) 4 for (miles): "))
# match b:
#     case 1:
#         print(a * 1000)
#     case 2:
#         print(a * 100000)
#     case 3:
#         print(a * 1000000)
#     case 4:
#         print(a * 0.621371)
#     case _:
#         print("Invalid")

a = input("Enter the A avlue in kilometer")
b = int(input("Enter the number 1 as(meter) 2 for (centimeter) 3 for (millimeter) and 4 for (miles)"))
match b:
    case 1:
        print( a * 1000)
    case 2:
        print(a * 100000)
    case 3:
        print( a * 1000000)
    case 4:
        print(a * 623171)
    case _:
        print("invalid Input")