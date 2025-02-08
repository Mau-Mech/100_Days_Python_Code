print("System for calculate the averange of each alumn")
name = input("What is your name (add the last name too please)?: ")

math_note =float(input("O.k "+ name + " What is your final note in math?: " )) #This value was int in the beggining so its possible to use float too.
chemistry_note = float(input("O.k "+ name + " What is your final note in chemistry?: "))
biology_note = float(input("O.k " + name + " What is your final note in biology?: "))

averange_note = (math_note + chemistry_note + biology_note) / 3
averange_note =float(averange_note)

if (averange_note > 5.9):
    print ("Congratulation!",name, "you final note is", averange_note, "you PASS the grade")
    print ("Congratulation!",name, "you final note is", round(averange_note,2), "you PASS the grade") #Here the system will show the average value with 2 decimals using the method round
else:
    print("Sorry" , name, "you final note is", round(averange_note,2), "you WONT pass")
print("Fin") 