class Alumno:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.nota = 0
        self.nacionalidad = ""

    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad

    def obtenerNota(self):
        return self.nota

    def leerNota(self):
        while True:
            nota = input(f"Alumno {self.nombre} {self.apellido}, Ingrese nota: ")
            if not nota.isnumeric():
                print("Nota incorrecta, vuelva a intentarlo")
            elif int(nota) >=0 and int(nota) <=20:
                self.registrarNota(nota)
                break
            else:
                print("Nota incorrecta, vuelva a intentarlo")

    def registrarNota(self,nota):
        self.nota = nota
        

