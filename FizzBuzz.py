# TEACHER METHOD

target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# MY METHOD 

    values = 100

list = []
for i in range(101):
  if i % 3 == 0 and i % 5 == 0:
    list.append("FizzBuzz")
  elif i % 3 ==0 :
    list.append("Fizz")
  elif i % 5 == 0 :
    list.append("Buzz")
  else:
    list.append(i)
list.pop(0)

for x in list:
  print(x)   