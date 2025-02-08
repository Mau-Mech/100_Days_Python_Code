string = input("Please type any phrase: ")
delete_element = input("Which word or letter do you want to erease?: ")
length_of_word = len(delete_element)

location_element_to_delete = string.find(delete_element)

temp_string1 = string[0:location_element_to_delete]
temp_string2 = string[location_element_to_delete + length_of_word:]

temp_string1.rstrip(delete_element)
temp_string2.lstrip(delete_element)

print(temp_string1,temp_string2)