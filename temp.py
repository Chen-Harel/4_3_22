import re


regex = "^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"

userEmail = input("Enter your email to check validation: ")
for i in userEmail:
    if i =="@":
        userEmail=re.sub("@", "AT SYMBOL WAS HERE", userEmail)
    elif i=="$":
        userEmail=re.sub("$", "DOLLAR SIGN WAS HERE", userEmail) 
print(userEmail)
