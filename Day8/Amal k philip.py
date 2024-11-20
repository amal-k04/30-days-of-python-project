"""
Author:AMAL K PHILIP
Date:20-11-2024
Description:Python program to calculate the factorial of a given number.
"""

number=int(input("Enter a Positive number:"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print(f"The factorial of {number} is {factorial}")
