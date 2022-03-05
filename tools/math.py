from main import clearConsole

class Calc:
    def __init__(self):
        pass

    def addNums():
        sum = 0
        n1 = int(input("Enter the first number to add: "))
        n2 = int(input("Enter the second number to add: "))
        sum=n1+n2
        return sum  

    def subNums():
        sub = 0
        n1 = int(input("Enter the first number to subtract: "))
        n2 = int(input("Enter the second number to subtract: "))
        sub=n1-n2
        return sub

    def multNums():
        mult = 0
        n1 = int(input("Enter the first number to multiply: "))
        n2 = int(input("Enter the second number to multiply: "))
        mult=n1*n2
        return mult

    def divNums():
        div = 0
        n1 = int(input("Enter the first number to divide: "))
        n2 = int(input("Enter the second number to divide: "))
        div=n1/n2
        return div

    def fibonacci():
        pass

    def calcMenu():
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("5 - Show the fibonacci list")
        print("x - Quit to main menu")
        userChoice = input("What would you like to do? ").lower()
        clearConsole()
        if userChoice == "1":
            print(f"Your total is: {Calc.addNums()}")
        elif userChoice == "2":
            print(f"Your total is: {Calc.subNums()}")
        elif userChoice == "3":
            print(f"Your total is: {Calc.multNums()}")
        elif userChoice == "4":
            print(f"Your total is: {Calc.divNums()}")
        elif userChoice == "5":
            Calc.fibonacci()
        elif userChoice == "x":
            return
        else:
            print("Please select an option from the list.")