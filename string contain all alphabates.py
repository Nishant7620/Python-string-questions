#Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").
#If it does, print True. Else, print False. Before comparing the characters, you should convert the string to lowercase.
#If the string contains spaces, ignore them before finding the result.
#You may assume that the string doesn't contain any other symbols, only spaces (possibly).
#Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz

import string
str = input("enter a string:")
s =set(str.lower())


