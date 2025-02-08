word_1 = "i am lord voldemort" #input(str("Please type the first word: "))
word_2 = "tom marvolo riddle"

word_1 = word_1.lower()
word_2 = word_2.lower()

print(word_1)
print(word_2)

list_1 = list(word_1)
list_2 = list(word_2)

list_1.sort()
list_2.sort()

#print(list_1)
#print(list_2)

value = True


for index_1 in list_1:
    if " " in list_1:
        list_1.remove(" ")

for index_2 in list_2:
    if " " in list_2:
        list_2.remove(" ")

#print(len(list_1))
#print(list_1)
#print(list_2)

for index_3 in range(0 , len(list_1)):
    if list_1[index_3]!=list_2[index_3]:
        value = False
        #print(f"comparison list 1: {list_1[index_3]} y list 2: {list_2[index_3]}")
        break
    else:
        value = True

print(value)