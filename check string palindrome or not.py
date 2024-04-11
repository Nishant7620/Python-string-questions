#Write a Python function that takes in a string and checks if it is a palindrome. 
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, 
# ignoring spaces, punctuation, and capitalization.


string = input("enter a string:")
# new_string = string.replace(" ","")
new_string= string.lower()
# temp =""

# for char in new_string:
#     temp = char + temp
# print(new_string)    
# print(temp)
# if temp == new_string:
#     print("True")
# else:
#     print("False")  

print(new_string)

reverse_string=new_string[::-1]
print(reverse_string)
if new_string == reverse_string:
    print("True")
else:
    print("false")   


new_string = "A man, a plan, a canal, Panama"

          



# for char in string:
#     temp = char + temp

   

