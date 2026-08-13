##Logica de la calculadora

#Titulo 
print("======INGRESE NOTAS Y PONDERACIONES======\n")

#Lista de diciconarios para almacenar las notas y ponderaciones
evaluaciones = []

#Funcion para calcular el aporte 
def calcular_aporte(nota, ponderacion):
    ponderacion /= 100
    resultado = round((nota * ponderacion), 2)
    return resultado


#Pedir al usuario nota y ponderacion
continuar = True
i = 0
aporte_total = 0
porcentaje_evaluado = 0
while continuar:
    evaluacion = input("Ingrese nombre de la evaluacion: ")
    nota = int(input("Ingrese la nota: "))
    ponderacion = int(input("Ingrese la ponderacion (%): "))
    evaluaciones.append({
        "nombre": evaluacion,
        "nota": nota,
        "ponderacion": ponderacion
    })

    #Sumar aportes de todas las evaluaciones
    nota = evaluaciones[i]["nota"]
    ponderacion = evaluaciones[i]["ponderacion"]
    porcentaje_evaluado += ponderacion
    resultado = calcular_aporte(nota, ponderacion)
    aporte_total += resultado
    i += 1
    continuar = input("¿Desea ingresar otra evaluacion? (s/n): ")
    if continuar != "s":
        continuar = False

#Mostrar lista de evaluaciones con sus notas y ponderaciones
print("======LISTA DE EVALUACIONES======\n")
for evaluacion in evaluaciones:
    print("Evaluacion:", evaluacion["nombre"], "\nNota:", evaluacion["nota"], "\nPonderacion:", evaluacion["ponderacion"], "%")

#Mostrar aporte total y porcentaje evaluado
print("======APORTE TOTAL======\n")
print("Aporte total:", aporte_total)
print("Porcentaje evaluado:", str(porcentaje_evaluado) + "%")