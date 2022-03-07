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
        # Program to display the Fibonacci sequence up to n-th term
        nterms = int(input("How many terms? "))
        # first two terms
        n1, n2 = 0, 1
        count = 0
        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        # if there is only one term, return n1
        elif nterms == 1:
            print("Fibonacci sequence upto",nterms,":")
            print(n1)
        # generate fibonacci sequence
        else:
            print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    
    def biggestNum():
            inp = input("Enter the numbers separated by a space ").split()
            int_list = list(map(int, inp))
            print ("Max number:",max(int_list))                 

    def calcMenu():
        while(True):
            print("1 - Add")
            print("2 - Subtract")
            print("3 - Multiply")
            print("4 - Divide")
            print("5 - Show the fibonacci sequence")
            print("6 - Get biggest num from multiple numbers")
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
            elif userChoice == "6":
                Calc.biggestNum()
            elif userChoice == "x":
                return
            else:
                print("Please select an option from the list.")