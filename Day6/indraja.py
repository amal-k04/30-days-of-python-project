'''
Authour:Indraja M S
Date:18-11-24
Description:A program that takes a string and reverses
 it using a for loop.
'''
string=input("Enter the string:")
reverse=" "
for i in string:
  reverse=i+reverse
print("reverse string",reverse)