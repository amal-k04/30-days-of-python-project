#AUTHOR=CYRIL JACOB THOMAS
#DATE=23-11-2024
#DESCRIPTION=Write a Python program to generate the Fibonacci sequence up to a specified number of terms.

num=int(input("Enter the number"))
for i in range(0,num):
    if i == 0:
        a=0
        b=1
        print(a,end=" ")
        print(b,end=" ")
    else:
        print(a+b,end=" ")
        temp=a
        a=b
        b=temp+b