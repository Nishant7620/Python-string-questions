#Write a Python program that prints the character at index i in the string s. 
#If the index is out of range, the program should print "i is out of range".
#If the string is empty, the program should print "Empty String".

string = input("enter a string: ")
i = int(input("enter index value: "))
if len(string) == 0:
    print("empty string")

else:
    if i>len(string) :
        print("i is out of range")
    else:
        if string[i] in string:
            print(string[i])    

