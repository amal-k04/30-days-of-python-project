"""
Author:Amal K Philip
Date:18-11-2024
Description:program that takes a string and reverses it using a for loop.
"""

string=input("enter the string:")
new_string=""

for i in range(-1,-len(string)-1,-1):
    new_string=new_string+string[i]
    
print(new_string)