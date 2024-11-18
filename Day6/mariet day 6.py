'''
author:Mariet Rose George
date:19/11/24
Description:reversing a string
'''
string=input("enter a string")
reverse=" "
for i in string:
    reverse=i+reverse
    print("reverse string is",reverse)