def is_leap_year(year):
    # Write your code here. 
    if (year % 4 == 0 and year % 100 != 0):
        return True 
        
    elif (year % 100 == 0 and year % 400 == 0):
            return True
    else:
        return False


year = [2000,1885,2025,4000,1995,1870,1578,2020,2024]

for value in year:
    print(is_leap_year(value))


# 1 Revisar como lo hice anteriormente
# 2 Checar el metodo Switch
# Complejidad en tiempo y en espacio 
