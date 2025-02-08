#MY METHOD
number = int(input("Enter a number between 0 and 1000: "))

if number > 1000 and number < 1:
    print("The value is not in range please repeat: " )

even_numbers = []
for index in range(number+1):
    if index %2 == 0:
        even_numbers.append(index)

print(even_numbers[1:])


print(sum(even_numbers))

#EXERCISE METHOD 2

even_sum = 0
for num in range(2, number + 1, 2):
  even_sum += num
print(even_sum)