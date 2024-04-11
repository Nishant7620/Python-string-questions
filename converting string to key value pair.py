#Write a Python function that takes in a string and returns the count 
# of each unique character in the string.
# The function should return the count of characters as a dictionary, 
# where the keys are the unique characters and the values are their respective counts. 
# Ignore spaces and consider uppercase
# and lowercase letters as different characters.

keys = input("enter a string")

default_value = 1


dictionary=dict.fromkeys(keys,default_value)
print(dictionary)