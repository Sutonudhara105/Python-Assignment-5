first_list=list()
second_list=list()
n=int(input("Enter the size of the List: "))
print("Enter the Element of first list: ")
for i in range(int(n)):
   k=int(input(""))
   first_list.append(k)
print("Enter the Element of second list: ")
for i in range(int(n)):
   k=int(input(""))
   second_list.append(k)
   final_list = [y for x in [first_list,second_list] for y in x] 
print ("Concatenated list using list comprehension: "+ str(final_list))  
 

                                   
   
