#declaration of numbers
x = 0
y = 0

#Welcome message
print("---Simple Calculator--")
print("-------Welcome--------")
print("for using this calculator pleas enter the values of 2 numbers")

#The user puts the nomber he want to do operations on
x = int(input("Enter value of number 1: " ))
y = int(input("Enter value of number 2: " ))

#Simple menu
print("Select the operation you want to use:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division")

try:
    selection = int(input("Select the number of the operation: "))
    if selection < 1 or selection > 4:
        print("Invalid selection")
        exit()
except ValueError:
    print("Please enter a valid number for selection.")
    exit()

#Selection of number
match selection:
    case 1: 
        addition = x + y
        print("The result is : ", addition )
    case 2:
        subtraction = x - y
        print("The result is : ", subtraction )
    case 3:
        multiplication = x*y
        print("The result is : ", multiplication )
    case 4:
        division = x/y
        print("The result is : ", division )