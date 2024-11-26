'''
Author:Amal k philip
Date:26-11-2024
Description:Python program to find all pairs of numbers in a list that add up to a specific sum,
            without repeating the value in different order.
'''
#listing the element
lis=[]
n=int(input("enter no: Elements:"))
while n>0:
    num=int(input("enter the element:"))
    lis.append(num)
    n=n-1

sum=int(input("enter a sum:"))
#finding the sum of 2 elements and ordering
sum_list=[]
for i in lis:
    for k in lis:
        if i+k==sum:
            (a,b)=(i,k)
            if (a,b)==(k,i):
                pass
            else:
                sum_list.append((i,k))

j=len(sum_list)//2
#printing the output and not repeating the elements in different order. 
print(sum_list[0:(j)])