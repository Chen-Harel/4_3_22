import tools.math as myMath
import tools.strings as myString
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def main():
    while(True):
        print("Welcome to my program, please select an option from the menu.")
        print("1 - Open calculator menu")
        print("2 - Open string menu")
        print("x - Quit")
        userChoice = input().lower()
        clearConsole()
        if userChoice == "x":return
        elif userChoice == "1":
            myMath.Calc.calcMenu()
        elif userChoice == "2":
            myString.Strings.stringMenu()
        else:print("Please choose an option fromt he menu.")

if __name__ == "__main__":
    main()