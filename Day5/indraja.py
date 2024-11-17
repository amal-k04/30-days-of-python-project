'''
Authour:Indraja M S
Date:17-11-2024
Description: A program to print the multiplication table of a given number using a while loop upto 10 times.
The result can display using print() function.
'''
num=int(input("Enter a number:"))
i=1
while i<=10:
    print(f"{num}×{i}={num*i}")
    i+=1