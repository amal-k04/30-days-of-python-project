"""
Author:AMAL K PHILIP
Date:19-11-2024
Description:program to count the number of digits in a given integer using a while loop. And Display the sum of digits.
"""

number=int(input("Enter the number:"))
sum=0
count=0

while number>0:
    count+=1
    digit=number%10
    sum=sum+digit
    number=number//10

print(f"Number of Digits:{count}")
print(f"Sum of Digit:{sum}")