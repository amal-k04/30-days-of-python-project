# Author:CYRIL JACOB THOMAS
# Date:20-11-2024
# Description:Write a Python program to calculate the factorial of a given number.


a=int(input("Enter the number: "))
fac=1
for i in range(2,a+1):
    fac=fac*i
print ("factorial of number is : ",fac)
