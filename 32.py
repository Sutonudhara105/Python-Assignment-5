list = []
f = False

count_list = int(input("Enter total numbers of the first list : "))

for i in range(count_list):
	no = int(input("Enter : "))
	list.append(no)

for i in range(len(list)):
    for j in range(len(list)):
        if  i != j:
            product = list[i] * list[j]
            if product & 1:
	            f = True
            

print("For the list", list,"odd product is",f)
