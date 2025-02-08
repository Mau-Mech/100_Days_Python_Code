def greet():
    print("Hola")
    print("Hi")
    print("Bounjour")
greet()


def greet_02(name_01, name_02, name_03):
    print(f"Hola {name_01}")
    print(f"Hi {name_02}")
    print(f"Bounjour {name_03}")

a = input("First name = ")    
b = input("Second name = ")    
c = input("Thirt name = ")    
greet_02(a,b,c)
