# Author:cyril
# Date:25-11-2024
# Description:This Python script checks whether a given number is a Palindrome and determines if it is Prime.

s=str(input("Enter string: "))
s1=s[::-1]
if s1==s:
    print("The number",s,"is palindrome")
else:
    print("The number",s,"is not palindrome")
u=int(s)
p=True
for i in range(2,u):
    if u%i==0:
        p=False
        
        break
if p==True:
    print("The number",s," is PRIME")
else:
    print("The number",s," is NOT PRIME")