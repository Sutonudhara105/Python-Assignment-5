a = list(map(int, input("Enter First list: ").split()))
b = list(map(int, input("Enter second list: ").split()))
c = [bxx for bxx in b if bxx not in a]
print("Required list: ",*c)
