def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
#result = outer_function(5, 10)
#print(result)

#print(outer_function(5, 10))


""" for c in range(1,4):
    for d in range (1,4):
     #print(c)
     print(outer_function(c,d+1)) """

for c,d in zip(range(1,4), range(1,4)):

     print(outer_function(c,d+1))