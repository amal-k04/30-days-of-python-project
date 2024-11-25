'''
Author:Amal k philip
Date:25-11-2024
Description:Python program checks whether a given number is a Palindrome and determines if it is Prime.
'''

num=int(input("Enter a number:"))

temp=num
reverse=0

while temp>0:
    digit=temp%10
    reverse=reverse+digit
    temp=temp//10
    reverse=reverse*10
reverse=reverse//10
if num==reverse:
    print(f"The number {num} is a Palindrome.")
else:
    print(f"The number {num} is not a Palindrome.")
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
    else:
        pass
if prime==True:
    print(f"The number {num} is a Prime number.")
else:
    print(f"The number {num} is not a Prime number.")