class Persona:

    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    def description(self):
        return '{} tiene {} años '.format(self.nombre,self.año)
    
    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)
    
doctor = Persona("Luis",30)

print(doctor.nombre)
print(doctor.description(), doctor.comentario("Probando las clases"))
    

    
