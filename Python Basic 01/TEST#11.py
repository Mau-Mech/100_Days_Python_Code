original_list = ["A","B","b","c","E","E","f"]
print(f"This is the original list: {original_list}")
element = input("Please type the element that you want to delete: ")

for _ in original_list:
   if element.lower() in original_list:
      original_list.remove(element.lower())
   elif element.upper() in original_list:
      original_list.remove(element.upper())

 
print(f"List with the element deleted: {original_list}")