# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
#curr_char and new_char are variables that contain strings with a single character. You may assume that new_char will not be an empty string. 
#The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
#If no match is found, print the initial string.

str = input("enter a string: ")
curr_char = input("enter charater you want to replace: ")
new_char = input("enter charater you want to add: ")

if new_char not in str:
    print(str)

else:
    if new_char in str:
        new_string = str.replace(curr_char,new_char)

        print(new_string)
