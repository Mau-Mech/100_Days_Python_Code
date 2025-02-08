squares = ["orange", "orange", "purple", "orange", "blue"]
newsquares = []
i = 0
while (squares[i] == "orange"):
    newsquares.append(squares[i])
    i = i+1
    print(i)
print(newsquares)

dates = [1982, 1980, 1973, 2000]
x = 0
year = dates[0]
while (year != 1973):
    print(year)
    x = x+1
    year = dates[x]

print(f"It took {x} repetitions to get out of loop")
