# Author=cyril
# description=a program that takes a string and reverses it using a for loop.
# Date=18/11/24

string=input("enter the string")
length=len(string)
for i in range (length-1,-1,-1):
     print(string[i],end="")
     
