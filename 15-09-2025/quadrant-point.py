# To finding the quadrant point in graph value of (x, y)

# a = int(input("Enter your x value: "))
# b = int(input("Enter your Y value: "))

# if a > 0 and b > 0:
#     print("Quadrant-1") 
# elif a < 0 and b > 0:
#     print("Quadrant-2")
# elif a < 0 and b < 0:
#     print("Quadrant-3")
# elif a > 0 and b < 0:
#     print("Quadrant-4")
# else:
#     ("Enter correct value")    

# To finding movie rating using ( match variable )

rating = int(input("Enter the movie rating: \n"))
match rating:
    case 1:
        print(" Very Bad")
    case 2:
        print("Bad")
    case 3:
        print("Good")
    case 4:
        print("Very Good")
    case 5:
        print("Excellent")
    case _:
        print("Invalid Rating ")

# To finding