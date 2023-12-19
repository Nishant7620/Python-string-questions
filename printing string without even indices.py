#Write a Python program that prints the string s without the characters located at even indices.
#If the string is empty or only has one character, print it intact


str = input("enter a string: ")

if len(str)<=0:
    print("empty string")

else:
    print(str[::2])