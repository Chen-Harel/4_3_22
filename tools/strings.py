import os
import re

clearConsole1 = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



class Strings:
    def __init__(self):
        pass
    
    def simpFunc():
        Name = input("Enter your name: ")
        age = input("Enter your age: ")
        print(f"Hello {Name}, you are {age} years old.")

    #Version 1
    def longestString():
        s1 = input("Enter the first string: ")
        s2 = input("Enter the second string: ")
        if len(s1) > len(s2):
            print(s1)
        else:
            print(s2)

    #Version 2
    def compare_strings_len(s1, s2):
        if len(s1) > len(s2):
            print('String 1 is longer: ', s1)
        elif len(s1) < len(s2):
            print('String 2 is longer: ', s2)
        else:
            print('Strings length are equal!')

    def stringReplace():
        inp = input("Enter a string: ")
        inp.replace("%", "_")
        inp.replace("$", "_")

    def emailValidateWithRegEx():
        regex = "^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
        userEmail = input("Enter your email to check validation: ")
        x=re.search(regex, userEmail)
        if x:
            print("Your word has one or more of the two symbols")
        else:
            print("Your word contains none of the two symbols.")

    def stringMenu():
        print("Welcome to the string text menu.")
        print("Choose an option from the menu.")
        print("1 - Print your name and age")
        print("2 - Check which string is longest.")
        print("3 - Replace string comlex way")
        print("4 - Replace string using RegEx")
        print("x - Exit to main menu")
        userChoice = input("What would you like to do? ")
        clearConsole1()
        if userChoice == "1":Strings.simpFunc()
        elif userChoice == "2":Strings.longestString()
        elif userChoice == "3":Strings.stringReplace()
        elif userChoice == "4":Strings.stringReplaceWithRegEx()
        elif userChoice == "x":return
        else:
            print("Please select an option from the menu...")
