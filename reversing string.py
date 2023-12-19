#Write a Python Program that prints the reversed version of a string. 
#The program must preserve uppercase and lowercase letters. If the string is empty, print it intact.

string = input("enter a string: ")

string_lower =string.lower()

if len(string_lower) ==0:
    print("string is empty")

else:
    print(string_lower[::-1])

