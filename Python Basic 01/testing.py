my_list = [10, 20, 20, 30, 20, 40]
 
#print(len (my_list))

new_list = []

for i in my_list:
    if i != 20:
       new_list.append(i)
 
print(new_list)  