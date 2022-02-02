n1=int(input("enter no of rows :"))
m1=int(input("enter no of columns :"))
print("enter the elements of first matrix :")
matrix_a=[[int(input())for i in range (m1)]for i in range (n1)]
for n in matrix_a:
    print(n)
n2=int(input("enter no of rows :"))
m2=int(input("enter no of columns :"))
if(n1==n2):
    print("enter the elements of second matrix :")
    matrix_b=[[int(input())for i in range (m1)]for i in range (n1)]
    for m in matrix_b: 
        print(m)
result=[[0 for i in range(m2)]for i in range(n2)]
for i in range(n2):
    for j in range (m2):
        for k in range (m1):
            result[i][j]=matrix_a[i][k]*matrix_b[k][j]
print("multiplication of two matrices :")
for r in result:
    print(r)
else:
    print("multiplication not allowed for this two matrices.")
