list = [1,"a",True,[1,2,3]]

element = list[3][1]
print(element)

nest = [1,"a", True, [1, 2,["f","g","h"]]]
new_element = nest[3][2][:]
print(new_element)