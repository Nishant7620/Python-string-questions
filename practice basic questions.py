#Write a Python program to count the number of vowels and consonants in a given string.

# str1 = input("enter a string")
# str1 =str1.lower()
# vowels = 0
# consonents = 0

# v = ['a','e','i','o','u']

# for char in str1:
#     if char.isalpha():     
#         if char in v:
#             vowels +=1
#         else:
#             consonents +=1

# print(f"number of vowels {vowels}")
# print(f"number of consotents {consonents}")


#Create a function that takes a string as input and returns the string reversed.

# string = input("enter a string: ")

# def users_input(string):
#     reverse_string = ""
#     for char in string:
#         reverse_string = char + reverse_string
#     return reverse_string    

# result = users_input(string)
# print(result)


#Write a program to check if two strings are anagrams of each other

# users_input_1 = input("enter a string:")
# users_input_1 = users_input_1.lower()
# users_input_2 = input("enter a string:")
# users_input_2 = users_input_2.lower()

# list_1 = list(users_input_1)
# list_2 = list(users_input_2)

# list_1.sort()
# print(list_1)
# list_2.sort()
# print(list_2)

# if list_1 == list_2:
#     print("anagrams")
# else:print("not anagrams")    


#Implement a function to remove all duplicates from a string and return the resulting string

user_input = input("enter a string: ")

result = ""

for char in user_input:
    if char not in result:
        result +=char
print(result)        


#Write a Python program to find the longest common prefix string amongst a list of strings.
#Create a function that takes a sentence as input and returns the number of words in the sentence.
#Write a program to check if a string is a palindrome.
#Implement a function to capitalize the first letter of each word in a sentence.
#Write a Python program to find the first non-repeated character in a given string.
#Create a function that takes two strings as input and returns True if one string is a rotation of the other, False otherwise.