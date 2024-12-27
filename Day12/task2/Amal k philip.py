"""
Author=Amal K Philip
Description=This Python program identifies the longest word in a given list of words. It also calculates and displays the length of that word
"""

sentence=input("enter the sentence:")
sentence=sentence.split()
print(sentence)
max=0
for i in sentence:
    if len(i)>max:
        max=len(i)
        large=i
print("The longest word is:",large)
print("Its length is:",max)
