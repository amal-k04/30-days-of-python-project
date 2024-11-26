'''
Author:Amal k philip
Date:26-11-2024
Description:Python program to convert a nested list into a flat list.
'''

nest_list=(input("enter a nested listed:"))
flat_list=[]
integer_list=["0",'1','2','3','4','5','6','7','8','9']

for list in nest_list:
    for element in list:
            if element in integer_list: 
                final_element=int(element)   
                flat_list.append(final_element)
print(flat_list)
