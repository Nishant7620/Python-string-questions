#Write a Python function that takes in a string and returns the count of vowels (a, e, i, o, u) in the string.
#  The function should ignore case, meaning it should count both uppercase and lowercase vowels.


string = input("enter a string")

vowels = ['a','e','i','o','u']


for i in vowels:
    if i in string:
        print(f"{i}: {string.count(i)}", end=' ')

          