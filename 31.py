dt2 =[]
dt =[]
d =[]
Number = int(input("Enter size of the list : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    dt2.append(value)

Numb = int(input("Enter size of the list : "))
for j in range(1, Numb + 1):
    value = int(input("Please enter the Value of %d Element : " %j))
    dt.append(value)

bxx=0
for bxx in dt:
    if(bxx not in dt2):
        d.append(bxx)

print("Required list is :",d)
