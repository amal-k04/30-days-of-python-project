AUTHOR = CYRIL
DESCRIPTION=a program to print the multiplication table of a given number using a while loop upto 10 times.The result can display using print() function.
DATE=17/11/24

num=int(input("ENter the number"))
i=1
while i<=10:
     print(f"{num} x {i} ={i*num}")
     i+=1
    
