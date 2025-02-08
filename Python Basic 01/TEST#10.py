Num_elem = int(input("Please type the length of the list: "))
List = []

for index in range(Num_elem):
    element = int(input(f"Please tipe the element number {index+1} of the list: "))
    List.append(element)

print(f"The List is created the values are: {List}")
print(f"The sum of all the elements are: {sum(List)}")
