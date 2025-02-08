#Create a program that determine if the "n" value is inside the list

def minor(value):
    list = [1,5,26,78,8,5,79,8,6,4,45,56,7895,12,2,9,10]
    for num in list:
        if num == value:
           return True

        
           

val_1 = int(input("Type the value that you are looking for: "))

if minor(val_1) == True:
    print("The value is in the list.")
else: 
    print("The value is NOT in the list.")


    