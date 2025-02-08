def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    final = name1+name2

    for character in final:
        quanty1 = final.count("t")
        quanty2 = final.count("r")
        quanty3 = final.count("u")
        quanty4 = final.count("e")
        quanty5 = final.count("l")
        quanty6 = final.count("o")
        quanty7 = final.count("v")
        quanty8 = final.count("e")
    final1 = quanty1 + quanty2 + quanty3 + quanty4
    final2 = quanty5 + quanty6 + quanty7 + quanty8
    total = str(final1)+str(final2)
    print(total)


a = "Kanye West"
b = "Kim Kardashian"

calculate_love_score(a,b)

