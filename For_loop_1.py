# family = ["Luis", "Nena","Mauricio","Mario","Patricia"]

# for index in family:
#     print(index)


# for index_2 in range(0,len(family)):
#     print (index_2)

number = [5 , 8, 9]
value = 0
for index in range(0, len(number)):
    number[index] = int(number[index])

    value += number[index]
    print(number[index])
print(value)
