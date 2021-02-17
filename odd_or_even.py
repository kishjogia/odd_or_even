number = input("Please enter a number: ")

if (number.isnumeric()):
    if (int(number) % 2) == 0:
        print (number + " is an even number")
    else:
        print (number + " is an odd number")
else:
    print ("The value enter is not a number")