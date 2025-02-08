import math

def distance(x1,x2,y1,y2):
   distance = math.isqrt((x2-x1)**2+(y2-y1)**2)
   print(round(distance, 2))

val1 = int(input("Type the first value: "))
val2 = int(input("Type the second value: "))
val3 = int(input("Type the thirt value: "))
val4 = int(input("Type the four value: "))

distance(val1,val2,val3,val4)