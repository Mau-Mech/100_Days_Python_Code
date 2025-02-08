length = int(input("What will be the length of the list?: "))

list = []

for val in range(length):
    list.append(int(input(f"Add he value {val+1} in the list ")))

print(f"list: {list}")
print(f"The final summatory its: {sum(list)}")
