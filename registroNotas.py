from alumnos import *

def registrarAlumno():
    nombre = input("Ingrese nombre de alumno: ")
    apellido = input("Ingrese el apellido de alumno: ")
    edad = input("Ingrese la edad de alumno: ")
    nacionalidad = input("Ingrese la nacionalidad del alumno: ")
    alumno = Alumno(nombre, apellido, edad, nacionalidad)
    return alumno

def calificarAlumnos(alumnos):
    for alumno in alumnos:
        alumno.leerNota()
    

def calcularPromedioNotas(alumnos):
    suma = 0
    numAlumnos= len(alumnos)
    for alumno in alumnos:
        suma = suma + alumno.obtenerNota()
    
    promedio = suma / numAlumnos
    
    print("El promedio de notas para " + str(numAlumnos) + " alumnos es: " + str(promedio))
        

def sumarNotasAlumnos(alumnos):
    suma = 0
    numAlumnos= len(alumnos)
    for alumno in alumnos:
        suma = suma + alumno.obtenerNota()
    
    print("La suma de notas de " + str(numAlumnos) + " alumnos es: " + str(suma))


if __name__=="__main__":

    print("Bienvenidos al registro de notas")
    comandosSistema = ['R', 'C', 'P', 'S', 'X']
    comando = ""
    alumnos = []

    while True:
        comando = input("Ingrese comando: ")
        if comando in comandosSistema:
            if comando == "R":
                alumno = registrarAlumno()
                alumnos.append(alumno)
            elif comando == "C":
                calificarAlumnos(alumnos)
            elif comando == "P" :
                calcularPromedioNotas()
            elif comando == "S":
                sumarNotasAlumnos()
            elif comando == "X":
                break
        else:
            print("Comando incorrecto, vuelva a intentarlo")

