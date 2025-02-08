def is_prime(num):
    prime = []
    difference = []
    if num == 1:
        return True
    else:
        for value in range(2,num):
            prime.append(value)
        #print(prime)
            
        for value_2 in prime:
            result = num % value_2
            #print(f"{num} % {value_2} = {result}")
            if result == 0:
                difference.append(1)
                #print(difference)
    if len(difference) <= 0:
        return True
    else: 
        return False



print(is_prime(48))