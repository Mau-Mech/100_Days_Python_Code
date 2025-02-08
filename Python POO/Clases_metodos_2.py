class Profesionista:
    def __init__ (self,edad,tipo,especialidad,trabajo):
        self.edad= edad
        self.tipo = tipo
        self.especialiad = especialidad
        self.trabajo = trabajo

Prof_1 = Profesionista(28,"Ingeniero" , "Mecanico", "Software")
Prof_2 = Profesionista(27,"Abogada","Penalista","Finanzas")

#print(Prof_1.tipo, Prof_2.tipo)
print("Antes era", Prof_2.tipo) 
setattr(Prof_2,"tipo","Contadora")
print("Ahora es", Prof_2.tipo)