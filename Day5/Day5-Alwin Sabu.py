'''
AUTHOR = ALWIN SABU
DESCRIPTION=a program to print the multiplication table of a given number using a while loop upto 10 times.The result can display using print() function.
DATE=17/11/24
'''
num=int(input("Enter number:"))
for i  in range (0,11):
    num2=num*i
    print(num,"*",i,"=",num2)
