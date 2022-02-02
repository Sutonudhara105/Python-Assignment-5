def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list

list1=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
list2=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    ele=int(input())
    list2.append(ele)
print(Union(list1, list2))