#Author=cyril
#DESCRIPTION=a program to count the number of digits in a given
#integer using a while loop.And Display the sum of digits.
#DATE=19/11/24


num=input("Enter the number")
length=0
i=0
while i < len(num):
    length+=1
    i+=1

print(length)
