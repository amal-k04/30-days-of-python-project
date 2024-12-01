sample=input("enter the statement:")
main_list=sample.split(" ")
sam=set(main_list)
for i in sam:
    count=0
    for j in main_list:
        if i==j:
            count+=1
    print(i,":",count)
