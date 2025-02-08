#PROGRAMA PARA CALCULAR EL NUEVO SALARIO DE UN TRABAJADOR SI OBTUO UN INCREMENTO DEL X%
def Salary (sal1,incre1):

    new_sal = sal1 + (sal1*(incre1/100))
    return new_sal


Actual_Salary = float(input("Type the actual salary of the worker: "))
Increase = float(input("Type the porcentage of the increase: "))
Salary_Updated = Salary(Actual_Salary,Increase)

print(f"The new salary will be : {round(Salary_Updated,2)}")