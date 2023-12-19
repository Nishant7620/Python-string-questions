7#Write a Python program that prints the first and last three characters of the string s as a single string. 
#If the string has less than six characters, print an empty string (blank output)

string = input("enter a string: ")
if len(string)<6:
    print(" ")
else:
    first_three = string[:3]
    last_three = string[-3:]

    print(first_three)
    print(last_three)    