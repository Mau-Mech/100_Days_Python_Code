class Email:
    def __init__(self): #Las funciones que estan dentro de las clases se llaman metodos
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()

print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)