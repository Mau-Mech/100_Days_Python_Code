def phrase_1(phrase):
    values = dict.fromkeys(phrase, 0)
    for index_1 in phrase:
        values[index_1] += 1

    #print(values)

    #key_to_delete=[key for key in values if key == " "]   # list comprehension syntaxis [expresión for elemento in iterable if condición]
    key_to_delete = []
    for index_2 in values:
        if index_2 == " ":
            key_to_delete.append(index_2)   

    for index_3 in key_to_delete:
       values.pop(index_3)

    print(values) 

    more_rep = max(values, key=values.get)
    print(f"The letter whom has more repetitions its {more_rep}, with {values[more_rep]}")

            


phrase_analize = str(input("Type the phrase that you want to count: "))
phrase_analize = phrase_analize.lower()
phrase_1(phrase_analize)


