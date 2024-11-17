"""
Author:Amal K Philip
Date:17-11-2024
Description:program to print the multiplication table of a given number using a while loop upto 10 times.
"""

num=int(input("enter the number:"))
i=1
while i<11:
    product=num*i
    print(num,"x",i,"=",product)
    i+=1