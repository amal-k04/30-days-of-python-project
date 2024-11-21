'''
author:Mariet Rose George
date:20/11/24
Description:count the number of digits
'''
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