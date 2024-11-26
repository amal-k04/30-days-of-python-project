'''
Author:Amal k philip
Date:21-11-2024
Description:Python program to generate the Fibonacci sequence up to a specified number of terms.
'''

limit=int(input("Enter the no: of terms in Fibonacci Series:"))
a=0
b=1
for times in range(0,limit):
    print(a,end=",")
    a,b=b,a+b
