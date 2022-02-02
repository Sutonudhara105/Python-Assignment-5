list=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    ele=int(input())
    list.append(ele)

min=max=list[0]
for i in range(1,len(list)):
    if list[i]<min:
        min=list[i]
    if list[i]>max:
        max=list[i]
print('Minimum Element in the list',list,'is',min)
print('Maximum Element in the list',list,'is',max)