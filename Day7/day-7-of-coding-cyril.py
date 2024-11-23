#Author=cyril
#DESCRIPTION=a program to count the number of digits in a given
#integer using a while loop.And Display the sum of digits.
#DATE=19/11/24


num=int(input("Enter the number"))
length=0
sum=0
i=0
while 0 < num:
    length+=1
    i+=1
    k=num%10
    sum=sum+k
    num=num//10
    
print(sum)
print(length)
