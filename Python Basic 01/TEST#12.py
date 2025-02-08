list = ["A","B","b","c","E","E","f"]
print(list)
last_elem = list.pop() #elimina ultimo elemento
first_elem = list.pop(0) #elimina primer elemento

new_list = [first_elem, last_elem]
print(f"This is the list with the elements delete: {list}")
print(f"This are the deleted elements: {new_list}")