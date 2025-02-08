#Function with positional arguments
#def greet_with(name,location):
#    print("Hello " + name)
#    print("What is it like in " + location)

#a = input("The name is?: ")
#b = input("The location is in?: ")

#greet_with(a,b)




#Function with keywords arguments
def greet_with(name,location):
    print("Hello " + name)
    print("What is it like in " + location)

a = "Mauricio"
b = "CDMX"

greet_with(name=a, location=b)