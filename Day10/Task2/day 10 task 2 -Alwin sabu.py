'''
Author ALWIN SABU
DATE=29/11/24
DESCRIPTION=This Python script checks whether a given number is a Palindrome and determines if it is Prime.
'''
# PalindromE
num=int(input("Enter the number"))
num2=num
rev=0
while num2>0:
    num3=num2%10
    rev=rev*10+num3
    num2=num2//10
if rev==num:
    print("The number",num,"is a palindrome number")
else:
    print("The number",num,"is not a palindrome number")



#Prime Number
num5=int(input("Enter the number "))
result=True
for i in range(2,num5):
    if num5%i!=0:
        result=False
        break
    else:
        continue
    
if result==True:
    print("The number",num5,"is a prime number")
if result==False:
    print("The number",num5,"is not a prime number")
